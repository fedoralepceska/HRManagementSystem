from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect
from .models import Department, DepartmentsChoices, Request, CustomUser
from HRManagementSystem.forms import DepartmentForm, CustomUserForm, RequestForm, HRForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.
def department_users(request):
    departments = Department.objects.all()
    users_by_department = {}
    for department in departments:
        users = department.employees.all()
        users_by_department[department.name] = users
    return render(request, 'department_users.html', {'users_by_department': users_by_department})


def create_department(request):
    if request.method == 'POST':
        if request.user.department == DepartmentsChoices.HR:
            form = DepartmentForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('department_users')
    else:
        form = DepartmentForm()
    return render(request, 'create_department.html', {'form': form})


def create_user(request):
    if request.method == 'POST':
        form = HRForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('home')
    else:
        form = HRForm()
    return render(request, 'accounts.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def add_request(request):
    user = request.user

    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save(user=user)
            return redirect('department_users')
    else:
        form = RequestForm()

    return render(request, 'add_request.html', {'user': user, 'form': form})


def hr_front(request):
    user = CustomUser.objects.get(pk=request.user.pk)
    remaining_days = 24 - user.usedVacDays - user.usedFreeDays
    return render(request, 'hrfront.html', {'user': user, 'remainingDays': remaining_days})


def index(request):
    return render(request, 'index.html')


def account(request):
    return render(request, 'accounts.html')


def inbox(request):
    return render(request, 'inbox.html')


def login_request(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                if user.department.name == DepartmentsChoices.HR:
                    return redirect("home")
                else:
                    # change this redirect to user default home page when it's implemented
                    return redirect("home")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    return render(request=request, template_name="login.html", context={"login_form": form})
