from django import forms
from .models import Signup, DropdownOption, Course, Section, Report, ViolationType, User, DenyReport, User
from django.forms import ModelForm
import random
import string

class SignupNow(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirmpass = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Signup
        fields = ['first_name', 'middle_initial', 'last_name', 'idnumber', 'email', 'password', 'confirmpass', 'program1', 'course', 'section', 'id_picture', 'registration_cert']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirmpass = cleaned_data.get("confirmpass")

        if password != confirmpass:
            raise forms.ValidationError("Passwords do not match.")

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['student', 'incident_date', 'violation_type']

class ViolationTypeForm(forms.ModelForm):
    class Meta:
        model = ViolationType
        fields = ['name', 'violation_type', 'description', 'guidelines', 'sanction_period_value', 'sanction_period_type']





from django import forms
from .models import User
import random
import string

class UserForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, label="First Name")
    middle_initial = forms.CharField(max_length=1, required=False, label="Middle Initial")
    last_name = forms.CharField(max_length=30, label="Last Name")
    suffix = forms.CharField(max_length=10, required=False, label="Suffix")
    position = forms.ChoiceField(choices=User.USER_CHOICES)
    email = forms.EmailField(label="Email")
    password = forms.CharField(widget=forms.PasswordInput, label="Password")

    class Meta:
        model = User
        fields = [
            'employee_id', 
            'first_name', 
            'middle_initial', 
            'last_name', 
            'suffix', 
            'position', 
            'email', 
            'password'
        ]

    def clean_employee_id(self):
        employee_id = self.cleaned_data['employee_id']
        if User.objects.filter(employee_id=employee_id).exists():
            raise forms.ValidationError("Employee ID already exists.")
        return employee_id

    def save(self, commit=True):
        user = super().save(commit=False)

        # Construct the full name
        full_name = f"{self.cleaned_data['first_name']} "
        if self.cleaned_data['middle_initial']:
            full_name += f"{self.cleaned_data['middle_initial']}. "
        full_name += f"{self.cleaned_data['last_name']}"
        if self.cleaned_data['suffix']:
            full_name += f", {self.cleaned_data['suffix']}"

        # Assign constructed full name to employee_name
        user.employee_name = full_name

        # Set and hash the password
        password = self.cleaned_data['password']
        user.set_password(password)

        if commit:
            user.save()
        return user

class DenyReportForm(forms.ModelForm):
    class Meta:
        model = DenyReport
        fields = ['date', 'student_id', 'violation', 'violation_type', 'reasons']
        labels = {
            'reasons': 'Reason(s) for denying this report:',
        }
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'reasons': forms.Textarea(attrs={'rows': 4}),
        }