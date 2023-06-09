# Generated by Django 4.2.1 on 2023-05-15 12:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HRManagementSystemApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='employees',
        ),
        migrations.RemoveField(
            model_name='department',
            name='employees',
        ),
        migrations.AddField(
            model_name='customuser',
            name='company',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='HRManagementSystemApp.company'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='date_employment',
            field=models.DateField(blank=True, default='2020-12-12'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='department',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='HRManagementSystemApp.department'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='usedFreeDays',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='usedSickLeave',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='usedVacDays',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
