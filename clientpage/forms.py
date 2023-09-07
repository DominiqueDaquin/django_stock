from django import forms
from .models import Compte,Pannier
class InscriptionForm(forms.ModelForm):
    class Meta:
        model=Compte
        fields=['nom','mdp','photo']

class ConnexionForm(forms.ModelForm):
    class Meta:
        model=Compte
        fields=['nom','mdp',]

class AjouterPannierForm(forms.Form):
        quantite=forms.IntegerField()
       
