from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.models import ModelForm
from .models import Post


mychoices = [('I', 'Imran'), ('KB', 'KB'), ('Alex', 'Alex')]
class SignUpForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class MyTestForm(forms.Form):
    name = forms.CharField(required=True, label='First Name')
    email = forms.EmailField()
    random = forms.CharField(widget= forms.Textarea())
    

class CreatePostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body', 'date_created', 'owner')

        