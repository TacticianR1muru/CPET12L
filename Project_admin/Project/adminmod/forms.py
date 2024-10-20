from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['employee_id', 'employee_name', 'position']

    def clean_employee_id(self):
        employee_id = self.cleaned_data['employee_id']
        if User.objects.filter(employee_id=employee_id).exists():
            raise forms.ValidationError("Employee ID already exists.")
        return employee_id