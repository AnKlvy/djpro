from django import forms
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
            , 'description': forms.Textarea(attrs={'cols': 60, 'rows': 10, 'class': 'form-control'})
            , 'is_published': forms.CheckboxInput(attrs={'class': 'form-check-input'})
            , 'categories': forms.SelectMultiple(attrs={'class': 'form-control'})
        }

    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) > 200:
            raise ValidationError('Length more than 200 characters ')
        return name
    # name = forms.CharField(max_length=255, label='Nammmme', widget=forms.TextInput(attrs={'class': 'form-control'}))
    # slug = forms.SlugField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10, 'class': 'form-control'}))
    # is_published = forms.BooleanField(required=False, initial=True,
    #                                   widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    # categories = forms.ModelChoiceField(queryset=PostCategories.objects.all(), empty_label='Category not selected',
    #                                     widget=forms.SelectMultiple(attrs={'class': 'form-control'}))
