from django.contrib import admin
from .models import *

class ListandoProdutos(admin.ModelAdmin):
    list_display = ('id', 'nome_produto', 'categoria')
    list_display_links = ('id', 'nome_produto')

admin.site.register(Produto, ListandoProdutos)