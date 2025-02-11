from django.urls import path
from . import views

urlpatterns = [
    path("c_mas_mas/", views.c_mas_mas),
    path("go/", views.go),
    path("python/", views.python),
    path("recibir_puntos_python/", views.recibir_puntos_python),
    path("recibir_puntos_c_mas_mas/", views.recibir_puntos_c_mas_mas),
    path("recibir_puntos_go/", views.recibir_puntos_go),
]