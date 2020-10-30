from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Anggota(models.Model):
    nama_anggota = models.CharField(max_length=100)
    nim_anggota = models.IntegerField(default=0)

    def __str__(self): 
        return self.nama_anggota
