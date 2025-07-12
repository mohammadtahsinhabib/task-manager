from django.contrib.auth.forms import UserCreationForm
import re
from django.contrib.auth.models import User , Group , Permission
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from tasks.forms import StyledFormMixin

class RegistrationForm(StyledFormMixin,forms.ModelForm):
    password= forms.CharField(widget=forms.PasswordInput)
    confirm_password= forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ["username","first_name","last_name","email","password","confirm_password"]

    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_exists = User.objects.filter(email=email).exists()

        if email_exists:
            raise forms.ValidationError("Email already exists")

        return email

    def clean_password(self):
        password = self.cleaned_data.get('password')
        errors = []

        if len(password) < 8:
            errors.append('Password must be at least 8 character long')

        if not re.search(r'[A-Z]', password):
            errors.append(
                'Password must include at least one uppercase letter.')

        if not re.search(r'[a-z]', password):
            errors.append(
                'Password must include at least one lowercase letter.')

        if not re.search(r'[0-9]', password):
            errors.append('Password must include at least one number.')

        if not re.search(r'[@#$%^&+=]', password):
            errors.append(
                'Password must include at least one special character.')

        if errors:
            raise forms.ValidationError(errors)

        return password

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password') 
        confirm_password = cleaned_data.get('confirm_password') 

        if password != confirm_password: 
            raise forms.ValidationError("Both Password should be change")
        return cleaned_data


class LoginForm(StyledFormMixin, AuthenticationForm):
    def __init__(self, *arg, **kwargs):
        super().__init__(*arg, **kwargs)

class AssignmentForm(StyledFormMixin, forms.Form):
    role = forms.ModelChoiceField(
        queryset=Group.objects.all(),
        empty_label="Select a Role"
    )

class CreateGroupForm(StyledFormMixin, forms.ModelForm):
    permissions = forms.ModelMultipleChoiceField(
        queryset=Permission.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label='Assign Permission'
    )
    
    class Meta:
        model = Group
        fields = ['name', 'permissions']
