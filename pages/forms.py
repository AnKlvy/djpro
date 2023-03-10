from django import forms
from .models import *


# time create i update sozdayutsa avtomatom
class AddPostForm(forms.Form):
    name = forms.CharField(max_length=255, label='Nammmme', widget=forms.TextInput(attrs={'class': 'form-control'}))
    slug = forms.SlugField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10, 'class': 'form-control'}))
    is_published = forms.BooleanField(required=False, initial=True,
                                      widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    categories = forms.ModelChoiceField(queryset=PostCategories.objects.all(), empty_label='Category not selected',
                                        widget=forms.SelectMultiple(attrs={'class': 'form-control'}))
