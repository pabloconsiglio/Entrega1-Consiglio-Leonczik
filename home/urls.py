from home import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('hola/', views.hola),
    path('fecha-nacimiento/<int:edad>', views.calcular_fecha_nacimiento),
    path('fecha/',views.fecha, name= 'fecha'),
    path('mi-template/', views.mi_template),
    path('personas-casamiento/', views.personas_casamiento, name = 'personas_casamiento'),
    path('crear-persona/', views.crear_persona, name='crear_persona'),
    
]

