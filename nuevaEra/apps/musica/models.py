from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Artista(models.Model):
    nombre = models.CharField(blank=False, max_length=100)
    
    def __unicode__(self):
        return self.nombre

class Tema(models.Model):
    usuario = models.ForeignKey(User)
    artista = models.ForeignKey(Artista)
    titulo = models.CharField(blank=False, max_length=100) 
    datetime = models.DateTimeField(blank=True, auto_now_add=True)
    link = models.CharField(blank=False, max_length=300)
    
    def __unicode__(self):
        return self.titulo

class Comentario(models.Model):
    usuario = models.ForeignKey(User)
    tema = models.ForeignKey(Tema)
    contenido = models.TextField(blank=False, max_length=500)
    
    def __unicode__(self):
        return self.contenido