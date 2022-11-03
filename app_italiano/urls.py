
#from core.erp.views.views import connsql,DasboardView,DasboardView2,DasboardView3
#from core.erp.views.ventas.ventas import Ventas
from django.urls import path
from . import views
from app_italiano.views import Juego,Listadeverbos,Conjugaciones#,Resultados

app_name = 'app_italiano'

urlpatterns = [
    #path('cobranzas/',connsql),
    path('juegotraduccionitaliano',Juego.as_view()),
    #path('resultados',Resultados.as_view()), # ESTO SOLO SE USA PARA CARGAR LOS VERBOS A LA BBDD.
    path('respuesta',views.Juego.formulario_traduccion),
    path('verboconjugado',views.Conjugaciones.formulario_conjugacion),
    path('conjugaciones',Conjugaciones.as_view()),
    path('listadeverbos',Listadeverbos.as_view()),
    path('about',views.about),

]