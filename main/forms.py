from  django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username","email","password1","password2")

    username = forms.CharField(max_length=50,widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Enter your username',
    }))    

    email = forms.EmailField(max_length=50,widget=forms.EmailInput(attrs={
        'class':'form-control',
        'placeholder':'Enter your email',
    }))    

    password1 = forms.CharField(max_length=50,label='Password',widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder':'Enter your password',
    }))    

    password2 = forms.CharField(max_length=50,label='Retype Password',widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder':'Confirm your password',
    }))    

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email address is already registered.")
        return email
    