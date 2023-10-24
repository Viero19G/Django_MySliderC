from django import forms
from .models import Perfil
 
 
# creating a form
class PerfilForm(forms.ModelForm):
 
    # create meta class
    class FormClass:
        # specify model to be used
        model = Perfil
 
        # specify fields to be used
        fields = '__all__'