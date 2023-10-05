from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Imagem)
admin.site.register(Video)
admin.site.register(Grade)
admin.site.register(Conteudo)
# admin.site.register(Perfil)
# admin.site.register(Perfil_Usuario)
# admin.site.register(Usuario)
admin.site.register(Setor)