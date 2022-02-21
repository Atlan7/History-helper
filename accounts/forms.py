from django import forms
from django.forms import ModelForm
from django.forms.widgets import FileInput
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError

from .models import Profile


class ImageWidget(forms.widgets.ClearableFileInput):
    template_name = "django/forms/widgets/file.html"


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(
        label='Имя пользователя',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    email = forms.EmailField(
        label='Введите email',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    password1 = forms.CharField(
        label='Введите пароль',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    password2 = forms.CharField(
        label='Подтверждение пароля',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control'
            }
        )
    )

    class Meta:
        model = Profile
        fields = ('username', 'email','password1', 'password2',)


#    def clean(self):
#        cleaned_data = super().clean()
#        if not is_teacher in cleaned_data and not is_student in cleaned_data:
#            raise ValidationError('Укажите ')
#        
#            raise ValidationError("Wrong date of birth!")
#        return date_of_birth


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Имя пользователя',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control'
            }
        )
    )


class UserProfileUpdateForm(forms.ModelForm):
    profile_image = forms.ImageField(
        label='Фотография профиля',
        required=False,
        widget=ImageWidget(
            attrs={
                'class': 'form-control',
            }
        )
    )
    bio = forms.CharField(
        label='О себе',
        required=False,
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'rows':7,
                'cols':15,
                'data-html': True,
                'placeholder': 'Напиши что нибудь о себе.'
            }
        )
    )


    class Meta:
        model = Profile
        fields = ('profile_image', 'bio',)
