from django.urls import path
from .views import home,galeria,formularioMascota, listar_mascotas, eliminar_mascota

urlpatterns =[
    path('', home, name="home"),
    path('galeria/', galeria, name="galeria"),
    path('formularioMascota/', formularioMascota, name="FormularioMascota"),
    path('listar-mascota/', listar_mascotas, name="listado_mascotas"),
    path('eliminar-mascota/<id>/', eliminar_mascota, name="eliminar_mascota"),
]
