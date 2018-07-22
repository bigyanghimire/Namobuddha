from django import forms
from .import models
class CreateArticle(forms.ModelForm):
    class Meta:
        model=models.File
        fields=['title','document','comments','category','status']

         
     