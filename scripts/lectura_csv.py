from ast import In
from tabnanny import verbose
from unittest import result
import pandas as pd
import random
import os

df_presente_simple = pd.read_csv('/home/danilo/Python/Django/italiano/csv/presente.csv')
df_passato_prossimo = pd.read_csv('/home/danilo/Python/Django/italiano/csv/passato_prossimo.csv')
df_futuro_semplice = pd.read_csv('/home/danilo/Python/Django/italiano/csv/futuro_semplice.csv')

df_traduccion = pd.read_csv('/home/danilo/Python/Django/italiano/csv/traduccion.csv')
df_traduccion.drop(['Unnamed: 0'], axis = 'columns', inplace=True)


def verbo_aleatorio(df):
    resultado=[]
    verbo=df.columns[random.randrange(1,df.shape[1],1)]
    persona=random.randrange(0,len(df[verbo])-1,1)
    dato = df.loc[persona,['Unnamed: 0',f'{verbo}']]
    resultado.append(verbo)
    resultado.append(dato[0])
    resultado.append(dato[1])

    return resultado

def traduccion(verbo,palabra_en_español):

    traducir = df_traduccion[f'{verbo}']

    if palabra_en_español in list(traducir):
        resultado = 'Correcto'
        
    else:
        resultado = 'Incorrecto'

    return verbo,list(traducir),resultado


##########################################################################################################################

correctas = 0
incorrectas = 0
listado_incorrectas = []

cantidad_verbos = df_presente_simple.shape[1]-1

while(cantidad_verbos != 0):
    os.system('clear')
    print(df_presente_simple.shape[1]-1)
    verbo = verbo_aleatorio(df_presente_simple)[0]
    print(f'Que significa la palabra: {verbo.upper()}')

    palabra = input('\nIngresa la traduccion: ') 
    elementos = traduccion(verbo,palabra)


    if elementos[2] == 'Correcto':
        correctas += 1
        print(f'{elementos[2].upper()}!!!!\n')
        print(f'Otros resultados posibles son: {elementos[1]}')

        print(f'\nCorrectas = {correctas}\nIncorrectas = {incorrectas}\n')
        df_presente_simple.drop([f'{verbo}'], axis = 'columns', inplace=True)

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
            print(f"- {i.upper()}, que significa: {list(df_traduccion[str(i)])}")
        break
        
print(f'\nFELICITACIONES!!!')
print('EJERCICIO COMPLETADO\n\nRESULTADO:')
print(f'\n- Correctas = {correctas}\n- Incorrectas = {incorrectas}\n') 
    