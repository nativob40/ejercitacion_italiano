
#from core.erp.views.views import connsql,DasboardView,DasboardView2,DasboardView3
#from core.erp.views.ventas.ventas import Ventas
from django.urls import path
from . import views
from app_italiano.views import DasboardView,Juego,Resultados

app_name = 'app_italiano'

urlpatterns = [
    #path('cobranzas/',connsql),
    path('',DasboardView.as_view()),
    path('juegotraduccionitaliano',Juego.as_view()),
    path('resultados',Resultados.as_view()),
    path('respuesta',views.Juego.formulario_traduccion),

]