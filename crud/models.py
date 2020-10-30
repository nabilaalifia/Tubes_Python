
from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Hewan(models.Model):
    jenis_hewan = models.CharField(max_length=100)
    usia_hewan = models.IntegerField(default=0)
    harga = models.IntegerField(default=0)

    def __str__(self):
        return self.jenis_hewan