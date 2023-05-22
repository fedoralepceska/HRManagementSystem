from django import forms
from HRManagementSystemApp.models import Department, CustomUser, Request
from django.contrib.auth.forms import AuthenticationForm


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name']


class CustomUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'department', 'date_employment', 'usedVacDays', 'usedSickLeave', 'usedFreeDays']


class HRForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'email', 'password', 'department', 'usedFreeDays', 'date_employment']
        labels = {
            'usedFreeDays': 'Your Free Days',
            'first_name': 'Name',
            'last_name': 'Surname',
            'date_employment': 'Date of Employment',
            'department': 'Job Position'
        }


class RequestForm(forms.ModelForm):
    num_days = forms.IntegerField()
    request_type = forms.ChoiceField(
        choices=[('free', 'Free Days'), ('sick', 'Sick Leave'), ('vacation', 'Vacation Days')])

    class Meta:
        model = Request
        fields = ('num_days', 'request_type',)

    def save(self, commit=True, user=None):
        request = super().save(commit=False)
        request.user = user
        request.save()

        if self.cleaned_data['request_type'] == 'free':
            user.usedFreeDays += self.cleaned_data['num_days']
        elif self.cleaned_data['request_type'] == 'sick':
            user.usedSickLeave += self.cleaned_data['num_days']
        elif self.cleaned_data['request_type'] == 'vacation':
            user.usedVacDays += self.cleaned_data['num_days']
        user.save()

        return request


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
