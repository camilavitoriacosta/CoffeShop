from django.urls import path
from . import views

urlpatterns = [
    path('cadastro_usuario', views.cadastro_usuario, name='cadastro_usuario'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('produtos', views.produtos, name='produtos'),
    path('cadastro_produtos', views.cadastro_produtos, name='cadastro_produtos'),
    path('deleta_produto/<int:produto_id>', views.deleta_produto, name='deleta_produto'),
    path('edita_produto/<int:produto_id>', views.edita_produto, name='edita_produto'),
    path('atualizar_produto', views.atualizar_produto, name='atualizar_produto')
]