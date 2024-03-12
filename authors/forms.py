from django import forms
from collections import defaultdict
from authors.validators import AuthorRecipeValidator
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from recipes.models import Recipe

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


class LoginForm(forms.Form):

    username = forms.CharField(
        label="Username",
    )

    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput()
    )


PREPARATION_TIME_UNIT = {
    'Minutos': 'Minutos',
    'Horas': 'Horas',
}

class AuthorRecipeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._my_errors = defaultdict(list)

    class Meta:
        model = Recipe
        fields = 'title', 'description', 'preparation_time', \
            'preparation_time_unit', 'servings', 'servings_unit', \
            'preparation_steps', 'cover'
        widgets = {
            'cover': forms.FileInput(),
            'servings_unit': forms.Select(
                choices=(
                    ('Servings', 'Servings'),
                    ('Number of people', 'Number of people'),
                ),
            ),
            'preparation_time_unit': forms.Select(
                choices=(
                    ('Minutes', 'Minutes'),
                    ('Hours', 'Hours'),
                ),
            ),
        }

    def clean(self, *args, **kwargs):
        super_clean = super().clean(*args, **kwargs)
        AuthorRecipeValidator(self.cleaned_data, ErrorClass=ValidationError)
        return super_clean

'''
class AuthorRecipeForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    title = forms.CharField(
        label="Title",
        required=True,
        min_length=3,
        error_messages={
            'min_length': 'Please, add more than 3 letters for the recipe title.',
            'required': 'Please fill in the recipe title.'
        }
    )

    description = forms.CharField(
        label="Description",
        required=True,
        min_length=3,
        error_messages={
            'min_length': 'Please, add more than 3 letters for the recipe description.',
            'required': 'Please fill in the recipe description.'
        }
    )

    preparation_time = forms.IntegerField(
        label="Preparation time",
        required=True,
        error_messages={
            'required': 'Please fill in the preparation time.'
        }
    )

    preparation_time_unit = forms.MultipleChoiceField(
        label="Preparation time unit",
        required=True,
        widget=forms.CheckboxSelectMultiple,
        choices=PREPARATION_TIME_UNIT,
    )

    servings = forms.CharField(
        label="Servings",
        required=True,
        error_messages={
            'required': 'Please fill in the number of servings.'
        }
    )

    servings_unit = forms.CharField(
        label="Servings unit",
        required=True,
        error_messages={
            'required': 'Please fill in the servings unit.'
        }
    )

    preparation_steps = forms.CharField(
        label="Preparation steps",
        required=True,
        error_messages={
            'required': 'Please fill in the servings unit'
        }
    )

    cover = forms.ImageField(
        label="Cover",
        required=True,
    )

    class Meta:
        model = Recipe
        fields = ('title', 'description', 'preparation_time', \
            'preparation_time_unit', 'servings', 'servings_unit', \
            'preparation_steps', 'cover')
        
    widgets = {
        'description': forms.Textarea,
        'preparation_time_unit': forms.CheckboxSelectMultiple,
        'cover': forms.FileInput,
    }
'''