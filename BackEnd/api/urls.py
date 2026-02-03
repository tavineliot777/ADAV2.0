from django.urls import path
from . import views

urlpatterns = [
    path("osso/listar", views.obter_osso),
    path("osso/criar/", views.criar_osso),
    path("osso/deletar/<int:pk>/", views.deletar_osso),
    path("osso/atualizar/<int:pk>/", views.atualizar_osso),
    path("osso/listar_todos/", views.obter_todos)
]