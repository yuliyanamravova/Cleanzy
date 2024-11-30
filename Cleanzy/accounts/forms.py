from django import forms
from django.conf import settings
from django.contrib.auth import get_user_model

from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm

user = get_user_model()


class CleanzyUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = user
        fields = ('username', 'email',)


class CleanzyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = user
        fields = ('username', 'email')


class CleanzyUserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'autofocus': True, 'placeholder': 'Email'}))
    password = forms.CharField(
        label="Password", widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'placeholder': 'Password'}),
    )
