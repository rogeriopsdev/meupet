from meupetApp.models import Perfil,Pet
from django import forms

class PerfilForms(forms.ModelForm):
    class Meta:
        model =Perfil
        fields = '__all__'

class PetForms(forms.ModelForm):
    class Meta:
        model=Pet
        fields ='__all__'

