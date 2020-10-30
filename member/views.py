from django.shortcuts import render, redirect
from member.models import *

# Create your views here. 
def index(request):
    siapa_ya = Anggota.objects.all()
    context_dict = {'nama_orang': siapa_ya}   
    return render(request, 'member/index.html', context_dict)