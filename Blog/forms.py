from .models import Blog
from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django.forms import widgets
from django.forms.forms import Form
from django.db.models import fields
from datetime import date, timedelta

class CreateBlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'
        widgets = {
            'DateofPublished': forms.DateInput(attrs={'type': 'date', 'value': date.today().strftime("%Y-%m-%d"),'readonly':True}),
        }

class UpdateBlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'
        widgets = {
            'BlogBame': forms.TextInput(attrs={'readonly':True}),
            'HostName' : forms.TextInput(attrs={'readonly':True}),
            'DateofPublished' : forms.DateInput(attrs={'readonly':True}),
        }