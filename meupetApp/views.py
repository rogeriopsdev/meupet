from django.shortcuts import render, redirect, get_object_or_404
from meupetApp.forms import PerfilForms, PetForms
from meupetApp.models import Perfil, Pet

# Create your views here.
def index(request):
    return render(request, 'app/index.html')

def new_perfil(request):
    perfis = Perfil.objects.all()
    form = PerfilForms(request.POST, request.FILES)
    if request.method=="POST":
        form = PerfilForms(request.POST, request.FILES)
        if form.is_valid():
            perfil =form.save()
            perfil.save()
            form= PerfilForms()
    return  render(request,'app/new_perfil.html',{'form':form, 'perfis':perfis })

def mostrar_perfil(request):
    perfis = Perfil.objects.all()

def editar_perfil(request,id):
    p = get_object_or_404(Perfil, pk=id)
    perfis = Perfil.objects.all()
    form = PerfilForms(instance=p)
    if request.method == "POST":
        form = PerfilForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            redirect('new_perfil')
        else:
            return render(request, 'app/editar_perfil.html', {'form': form, 'perfis': perfis, 'p': p})
    else:
        return render(request, 'app/editar_perfil.html', {'form': form, 'perfis': perfis,'p':p})