from django.db import models

class Article(models.Model):
    nom=models.CharField(max_length=20)
    prix=models.DecimalField(max_digits=10,decimal_places=2)
    quantite=models.IntegerField()
    photo=models.ImageField(upload_to='photosArticle/')
    id = models.AutoField(primary_key=True)
    
    def __str__(self):
        return self.nom