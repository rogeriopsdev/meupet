from django.db import models
import PIL
from PIL import Image

# Create your models here.
class Perfil(models.Model):
    id_perfil =models.AutoField(primary_key=True)
    nome_perfil = models.CharField(max_length=255)
    rg_perfil = models.CharField(max_length=255)
    nascimento_perfil = models.CharField(max_length=255)
    foto_perfil =models.ImageField(blank=True, null=True)
    def save(self):
        super().save()
        im= Image.open(self.foto_perfil)
        novo_tamanho = (80,80)
        im.thumbnail(novo_tamanho)
        im.save(self.foto_perfil.path)

    def foto_url(self):
        if self.foto_perfil and hasattr(self.foto_perfil, 'url'):
            return self.foto_perfil.url
        else:
            return self.nome_perfil
    def __str__(self):
        return self.nome_perfil

class Pet(models.Model):
    id_pet =models.AutoField(primary_key=True)
    foto_pet =models.ImageField(blank=True, null=True)
    matricula_pet =models.CharField(max_length=255)
    nome_pet= models.CharField(max_length=200)
    nascimento_pet = models.DateTimeField()
    id_perfil= models.ForeignKey(Perfil,models.DO_NOTHING, db_column='id_perfil')

    def __str__(self):
        return self.nome_pet


