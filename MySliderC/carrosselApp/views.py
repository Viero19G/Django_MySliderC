from django.shortcuts import render
 
# relative import of forms
from .models import Perfil
from .forms import PerfilForm
 
 
def create_view(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    form = PerfilForm(request.POST or None)
    if form.is_valid():
        form.save()
         
    context['form']= form
    return render(request, "create_perfil.html", context)