from django import forms
from crud.models import *

class Request(forms.ModelForm):
    jenis_hewan = forms.CharField(max_length=100)
    usia_hewan = models.IntegerField(default=0)
    harga = models.IntegerField(default=0)
    class Meta:
        model = Hewan
        fields = ('jenis_hewan','usia_hewan','harga')