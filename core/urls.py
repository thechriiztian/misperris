from django.urls import path
from .views import home,galeria,formularioMascota

urlpatterns =[
    path('', home, name="home"),
    path('galeria/', galeria, name="galeria"),
    path('formularioMascota/', formularioMascota, name="FormularioMascota")
    
]
