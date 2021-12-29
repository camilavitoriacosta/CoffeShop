from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagina_inicial,name='pagina_inicial'),
    path('catalogo_produtos/coffe', views.catalogo_produtos_coffe, name='catalogo_produtos_coffe'),
    path('catalogo_produtos/tea', views.catalogo_produtos_tea, name='catalogo_produtos_tea'),
    path('catalogo_produtos/smoothie', views.catalogo_produtos_smoothie, name='catalogo_produtos_smoothie'),
    path('buscar_produto', views.buscar_produto, name='buscar_produto'),
    path('cadastro_produtos', views.cadastro_produtos, name='cadastro_produtos'),
    path('deleta_produto/<int:produto_id>', views.deleta_produto, name='deleta_produto'),
    path('edita_produto/<int:produto_id>', views.edita_produto, name='edita_produto'),
    path('atualizar_produto', views.atualizar_produto, name='atualizar_produto'),
    path('produtos', views.produtos, name='produtos'),
    path('produtos_coffe', views.produtos_coffe, name='produtos_coffe'),
    path('produtos_tea', views.produtos_tea, name='produtos_tea'),
    path('produtos_smoothie', views.produtos_smoothie, name='produtos_smoothie'),
]