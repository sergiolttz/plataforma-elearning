from django.urls import path
from views import *

urlpatterns = [
    path("home/", pagina_inicio),
    path("login_registro", registro_login),
]