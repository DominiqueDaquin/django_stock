from rest_framework.response import Response
from rest_framework.decorators import api_view
from clientpage.models import Compte
from django.contrib.auth import login
@api_view(['POST'])
def login(request,nom,mdp):
    
    if request.method == 'POST':
        compte=Compte.objects.filter(nom=nom,mdp=mdp).first()
        if compte is not None:
            login(request,compte)
            
            return Response({
              'message': 'Hello, World!',
              'compte':compte.id
            })
        return Response({
           'message': 'Hello, World!'
        })