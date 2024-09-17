from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Customer

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
    
from django import forms

class RecordForm(forms.ModelForm):
    first_name = forms.CharField(required=True, max_length=50,label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your first name'}))
    last_name = forms.CharField(required=True, max_length=50,label="",  widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your last name'}))
    address = forms.CharField(required=True, max_length=255,label="",  widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your address'}))
    city = forms.CharField(required=True, max_length=50,label="",  widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your city'}))
    state = forms.CharField(required=True, max_length=50,label="",  widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your state'}))
    zipcode = forms.CharField(required=True, max_length=10,label="",  widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your zipcode'}))

    class Meta:
        model = Customer
        fields = ["first_name", "last_name", "address", "city", "state", "zipcode"]
