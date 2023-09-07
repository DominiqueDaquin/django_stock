from django.urls import path
from django.conf.urls.static import static
from .views import index,ajouter,suprimer,afficher,modifier
from django.conf import settings
urlpatterns = [
    path('',index,name='index'),
    path('ajouter/',ajouter,name='ajouter'),
    path('suprimer/<article_id>',suprimer,name='suprimer'),
    path('afficher/<article_id>',afficher,name='afficher'),
    path('modifier/<article_id>',modifier,name='modifier'),
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)