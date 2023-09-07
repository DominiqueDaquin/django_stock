from django.db import models
from gestion.models import Article
class Compte(models.Model):
    nom=models.CharField(max_length=20)
    mdp=models.CharField(max_length=10)
    photo=models.ImageField(blank=True)

class Pannier(models.Model):
    articleid=models.ForeignKey(Article,on_delete=models.CASCADE,default=None)
    quantite=models.IntegerField()
    compte=models.ForeignKey(Compte,on_delete=models.CASCADE,default=None)