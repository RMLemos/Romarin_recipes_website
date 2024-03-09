from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(
        label="First Name *",
        min_length=3,
        max_length=30,
        required=True,
        error_messages={
            'min_length': 'Please, add more than 3 letters for your first name.',
            'required': 'Please fill in your first name.'
        }
    )

    last_name = forms.CharField(
        label="Last Name *",
        required=True,
        min_length=3,
        max_length=30,
        error_messages={
            'min_length': 'Please, add more than 3 letters for your last name.',
            'required': 'Please fill in your last name.'
        }
    )

    email = forms.EmailField(
        label="E-mail *",
        required=True,
        error_messages={
            'required': 'Please fill in your email address.',
        }
    )

    password1 = forms.CharField(
        label="Password *",
        strip=False,
        widget=forms.PasswordInput(),
        required=True,
        error_messages={
            'required': 'Please enter a password.'
        }
    )

    password2 = forms.CharField(
        label="Confirm Password *",
        strip=False,
        widget=forms.PasswordInput(),
        required=True,
        error_messages={
            'required': 'Please confirm your password.'
        }
    )

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'username', 'email',
            'password1', 'password2',
        )

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            self.add_error(
                'email',
                ValidationError('Email already exists.', code='invalid')
            )

        return email
    
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("The two password fields didn’t match.")
