from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import fields
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    
    class Meta(UserCreationForm):
        model=CustomUser
        fields=('username','email','first_name','age',)

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model=CustomUser
        fields=UserChangeForm.Meta.fields #to use all the field mentioned in the CustomUser model

