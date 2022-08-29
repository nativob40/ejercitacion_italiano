from django.db import models

# Create your models here.
class Traduccion_de_verbos(models.Model):

    verbo = models.CharField(max_length=40)
    traduccion_uno = models.CharField(max_length=40)
    traduccion_dos = models.CharField(max_length=40)
    form_verbo_traducido = models.CharField(max_length=40)
