from django import forms

class Formulario_traduccion(forms.Form):

    verbo = forms.CharField(max_length=40)
    verbo_traducido = forms.CharField(max_length=40)

