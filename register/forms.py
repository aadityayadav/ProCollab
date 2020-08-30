from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    user_name=forms.CharField(max_length=20)
    user_email=forms.EmailField()
    user_skills=forms.CharField(max_length=150)
    user_github=forms.URLField(required=False)
    user_linkedin=forms.URLField(required=False)
    user_img=forms.ImageField()
    user_cv=forms.FileField(required=False)

    class Meta:
        model=User
        fields=["username","user_email","user_skills","user_github","user_linkedin","user_img","user_cv","password1","password2"]
