from django.urls import path
from . import views

urlpatterns = [
    path("mostrar_perfil/", views.mostrar_perfil),
    path("agregar_info", views.agregar_info),
]