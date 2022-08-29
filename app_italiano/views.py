from multiprocessing.sharedctypes import Value
from optparse import Values
from unicodedata import name
from django.shortcuts import render
from django.views.generic import TemplateView
from django import http
from django.http import HttpResponse
from django.template import loader
import pandas as pd
from script.lectura_csv import *
from app_italiano.forms import Formulario_traduccion
from app_italiano.models import Traduccion_de_verbos
import copy


# Create your views here.


df_presente_simple = pd.read_csv('script/csv/presente.csv')
#df_passato_prossimo = pd.read_csv('/home/danilo/Python/Django/italiano/csv/passato_prossimo.csv')
#df_futuro_semplice = pd.read_csv('/home/danilo/Python/Django/italiano/csv/futuro_semplice.csv')

df_traduccion = pd.read_csv('script/csv/traduccion.csv')
df_traduccion.drop(['Unnamed: 0'], axis = 'columns', inplace=True)
    

class Juego(TemplateView):
    
    template_name = 'juego_traduccion_italiano.html'

    correctas = 0
    incorrectas = 0
    listado_incorrectas = []

    def formulario_traduccion(request):
            
        if request.method == "POST":
            mi_formulario = Formulario_traduccion(request.POST)

            if mi_formulario.is_valid():
                datos = mi_formulario.cleaned_data
                verbo = Verbo.traduccion(verbo=datos['verbo'],palabra_en_español=datos['verbo_traducido'])
                
                if verbo[2]=='Correcto':
                    Juego.correctas += 1
                    verbo_eliminar = datos['verbo']
                    df_presente_simple.drop([f'{verbo_eliminar}'], axis = 'columns', inplace=True)
                    return render(request, 'respuesta_correcta.html',{'dato':datos})
                else:
                    Juego.incorrectas += 1
                    Juego.listado_incorrectas.append(verbo)
                    return render(request, 'respuesta_incorrecta.html',{'dato':datos})
                                                                      

  
        return render(request, "juego_traduccion_italiano.html")


    def get_context_data(self, **kwargs):
        
        v_aleatorio = Verbo.verbo_aleatorio(df_presente_simple)[0]   
        context = super().get_context_data(**kwargs)

        ###########
        context['etiqueta'] = v_aleatorio.upper()
        context['input_oculto'] = v_aleatorio
        ########### Tabla de Resultados ###########
        context['cantidad_de_verbos'] = df_presente_simple.shape[1]-1
        context['correctas'] = Juego.correctas
        context['incorrectas'] = Juego.incorrectas
        context['tabla_significado'] = Juego.listado_incorrectas
        

        
        return context








'''
    def juego_traduccion():
        correctas = 0
        incorrectas = 0
        listado_incorrectas = []

        cantidad_verbos = Verbo.df_presente_simple.shape[1]-1

        while(cantidad_verbos != 0):
            
            print(Verbo.df_presente_simple().shape[1]-1)
            verbo = Verbo.verbo_aleatorio(Verbo.df_presente_simple)[0]
            print(f'Que significa la palabra: {verbo.upper()}')

            palabra = input('\nIngresa la traduccion: ') 
            elementos = Verbo.traduccion(verbo,palabra)


            if elementos[2] == 'Correcto':
                correctas += 1
                print(f'{elementos[2].upper()}!!!!\n')
                print(f'Otros resultados posibles son: {elementos[1]}')

                print(f'\nCorrectas = {correctas}\nIncorrectas = {incorrectas}\n')
                Verbo.df_presente_simple.drop([f'{verbo}'], axis = 'columns', inplace=True)

            else:
                incorrectas += 1
                print(f'{elementos[2].upper()}!!!!\n')
                print(f'Palabras correctas son: {elementos[1]}')

                print(f'\nCorrectas = {correctas}\nIncorrectas = {incorrectas}\n')

                listado_incorrectas.append(verbo)
                
            cantidad_verbos -= 1

            salir = input('Desea Salir? S/N\n')  
            
            if salir == 's':
                print(f'\nPALABRAS INCORRECTAS:')
                for i in set(listado_incorrectas):
                    print(f"- {i.upper()}, que significa: {list(Verbo.df_traduccion[str(i)])}")
                break
                
        print(f'\nFELICITACIONES!!!')
        print('EJERCICIO COMPLETADO\n\nRESULTADO:')
        print(f'\n- Correctas = {correctas}\n- Incorrectas = {incorrectas}\n')
'''



class Resultados(TemplateView):
    
    template_name = 'resultados.html'



class DasboardView(TemplateView):
    
    template_name = 'index.html'

    df_presente_simple = pd.read_csv('script/csv/presente.csv')
        #df_passato_prossimo = pd.read_csv('/home/danilo/Python/Django/italiano/csv/passato_prossimo.csv')
        #df_futuro_semplice = pd.read_csv('/home/danilo/Python/Django/italiano/csv/futuro_semplice.csv')

        #df_traduccion = pd.read_csv('/home/danilo/Python/Django/italiano/csv/traduccion.csv')
        #df_traduccion.drop(['Unnamed: 0'], axis = 'columns', inplace=True)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ###########
        context['nombre'] = 'Danilo Devia'#self.payterms()
        context['verbo'] = Verbo.verbo_aleatorio(Verbo.df_presente_simple)[0]
        ###########

        
        return context


