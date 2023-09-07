from django.urls import path
from clientpage.views import index,accueil,pannier,ajouter_pannier,supprimer_pannier,connexion,acheter,facturation
from django.conf.urls.static import static
from django.conf import settings
app_name='clientpage'
urlpatterns = [
    path('',index,name='index'),
    path('accueil',accueil,name='accueil'),
    path('pannier',pannier,name='pannier'),
    path('ajouter_pannier/<article_id>',ajouter_pannier,name='ajouter_pannier'),
    path('supprimer_pannier/<id_article>',supprimer_pannier,name='supprimer_pannier'),
    path('connexion/',connexion,name='connexion'),
    path('acheter/',acheter,name='acheter'),
    path('facturation/<file>',facturation,name='facturation'),
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
