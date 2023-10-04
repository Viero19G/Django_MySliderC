# forms.py
from django import forms
from django.contrib.auth.models import Group

class GrupoForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name']
