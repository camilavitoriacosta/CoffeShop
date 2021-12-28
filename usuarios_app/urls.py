from django.urls import path
from . import views

urlpatterns = [
    path('cadastro_usuario', views.cadastro_usuario, name='cadastro_usuario'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('produtos', views.produtos, name='produtos'),
    path('cadastro_produtos', views.cadastro_produtos, name='cadastro_produtos')
]