from django import forms
from .models import Article
class AjouterArticle(forms.Form):
    nom=forms.CharField(max_length=20,label="nom de l'article")
    prix=forms.DecimalField(max_digits=10,decimal_places=2,label="prix de l'article")
    quantite=forms.IntegerField(label="nombres d'aticle en stock")
    photo=forms.ImageField()
    
class ModifierArticle(forms.ModelForm):
    class Meta:
        model=Article
        fields=['nom','prix','quantite','photo']