from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('', views.personas_view, name='personas'),
    path('crear/', views.crear_persona, name='crear_persona'),
    path('creada/', views.persona_creada, name='persona_creada'),
    path('listado/',views.lista_personas, name='lista_personas'),
]
