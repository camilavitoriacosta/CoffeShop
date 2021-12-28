from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('produtos_app.urls')),
     path('usuarios/', include('usuarios_app.urls')),
    path('admin/', admin.site.urls),
]
