from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import *


# time create i update sozdayutsa avtomatom
class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['categories'].empty_label = 'Category not selected'

    class Meta:
        model = Posts
        fields = ['name', 'slug', 'description', 'photo', 'is_published', 'categories']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'})
            , 'slug': forms.TextInput(attrs={'class': 'form-control'})
            , 'description': forms.Textarea(attrs={'cols': 60, 'rows': 6, 'class': 'form-control'})
            , 'is_published': forms.CheckboxInput(attrs={'class': 'form-check-input'})
            , 'categories': forms.SelectMultiple(attrs={'class': 'form-control'})
        }

    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) > 200:
            raise ValidationError('Length more than 200 characters ')
        return name


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    # name = forms.CharField(max_length=255, label='Nammmme', widget=forms.TextInput(attrs={'class': 'form-control'}))
    # slug = forms.SlugField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10, 'class': 'form-control'}))
    # is_published = forms.BooleanField(required=False, initial=True,
    #                                   widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    # categories = forms.ModelChoiceField(queryset=PostCategories.objects.all(), empty_label='Category not selected',
    #                                     widget=forms.SelectMultiple(attrs={'class': 'form-control'}))
