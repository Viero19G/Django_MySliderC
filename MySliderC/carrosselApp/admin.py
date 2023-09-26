from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Conteudo)
admin.site.register(Grade)
# admin.site.register(Perfil)
# admin.site.register(Perfil_Usuario)
# admin.site.register(Usuario)
admin.site.register(Setor)