from django.db import models

# Create your models here.
class Pet(models.Model):
    id_pet =models.AutoField(primary_key=True)
    matricula_pet =models.CharField(max_length=255)
    nome_pet= models.CharField(max_length=200)
    nascimento_pet = models.DateTimeField()