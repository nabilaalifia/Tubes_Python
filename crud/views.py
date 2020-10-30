from django.shortcuts import render, redirect 
from crud.models import *
from crud.forms import *
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def index(request):
    ambil_nama = Hewan.objects.all()
    form = Request()
    context = {'list_hewan': ambil_nama, 'form': form} 
    if request.method == 'POST':
        form = Request(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect('/crud/')
    else:
        print(form.errors)
    return render(request, 'crud/index.html', context)
        #return render(request, 'crud/index.html', context )
def delete(request,delname):
    names_from_db = Hewan.objects.all()
    form = Request()
    context_dict = {'names_from_context': names_from_db, 'form': form} 
    if request.method == 'POST':
        del_name = Hewan.objects.get(jenis_hewan = delname)
        del_name.delete()
    return HttpResponseRedirect('/crud/')
