from django.shortcuts import render
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