from django import forms
from .models import Tweet
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TweetForm(forms.ModelForm):
    class Meta:   #Standard practce of creating meta class in forms 
        model=Tweet
        fields=['text','photo'] #using list for custom forms in django
        
        
class UserRegistrationForm(UserCreationForm):
    email=forms.EmailField()
    class Meta:
        model=User
        fields=('username','email','password1','password2') #we are usig tupple in this case for built in forms in django