from django.urls import path
from . import views

urlpatterns = [
    path("home/",  views.pagina_inicio),
    path("login_registro",  views.registro_login),
]