from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Your Username', 'class': 'w-full p-2 my-2 mx-5 border border-gray-300 rounded-xl'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Your Email', 'class': 'w-full p-2 my-2 mx-5 border border-gray-300 rounded-xl'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Your Password', 'class': 'w-full p-2 my-2 mx-5 border border-gray-300 rounded-xl'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password', 'class': 'w-full p-2 my-2 mx-5 border border-gray-300 rounded-xl'}))