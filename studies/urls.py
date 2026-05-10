from django.urls import path
from .views import cadastrar_materia_view

app_name = 'studies'

urlpatterns = [
    path("nova-materia/", cadastrar_materia_view, name="cadastrar_materia")
]
