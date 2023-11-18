from django import forms
from carrosselApp.models import Planilha




class PlanilhaDeleteForm(forms.Form):
    confirmar_exclusao = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )