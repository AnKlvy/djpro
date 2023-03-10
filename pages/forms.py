from django import forms
from .models import *

# time create i update sozdayutsa avtomatom
class AddPostForm(forms.Form):
    name = forms.CharField(max_length=255)
    slug = forms.SlugField(max_length=255)
    content = forms.CharField(widget=forms.Textarea(attrs={'cols':60,'rows':10}))
    is_published= forms.BooleanField()
    categories= forms.ModelChoiceField(queryset=PostCategories.objects.all())