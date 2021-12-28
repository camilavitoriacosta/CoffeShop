from django.contrib import admin

from .models import *

class ListandoUsuarios(admin.ModelAdmin):
    list_display = ('id', 'email')
    list_display_links = ('id', 'email')

admin.site.register(Usuario, ListandoUsuarios)