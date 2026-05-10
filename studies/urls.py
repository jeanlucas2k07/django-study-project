from django.urls import path
from . import views
app_name = 'studies'

urlpatterns = [
    path("nova-materia/", views.cadastrar_materia_view, name="cadastrar_materia"),
    path("<int:materia_id>/", views.deleter_materia_view, name="deletar_materia"),
    path("editar/<int:materia_id>/", views.editar_materia_view, name="editar_materia"),
]
