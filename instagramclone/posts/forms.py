from django import forms
from .models import post

class CreateArticle(forms.ModelForm):
    class Meta:
        model = post
        fields = ['title','image']