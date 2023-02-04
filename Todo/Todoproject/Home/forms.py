from . models import Todo
from django import forms

class TodoForms(forms.ModelForm):
    class Meta:
        model=Todo
        fields=['name','date']