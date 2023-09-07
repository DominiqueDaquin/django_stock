from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import AjouterArticle,ModifierArticle
from .models import Article

def index(request):
    articles=Article.objects.all()
    return render(request,'index.html',locals())

def ajouter(request):
    
    if request.method=='POST':
        form=AjouterArticle(request.POST,request.FILES)
        if form.is_valid():
            nom=form.cleaned_data['nom']
            prix=form.cleaned_data['prix']
            quantite=form.cleaned_data['quantite']
            photo=form.cleaned_data['photo']
            article=Article(nom,prix,quantite,photo)
            article.save()
            sauvegarde=True
            articles=Article.objects.all()
            
            
            return redirect(reverse('index'),permanent=True)
            
            
    else:
        form=AjouterArticle()
    return render(request,'ajouter.html',locals())

def suprimer(request,article_id):
    articles=Article.objects.all()
    article=articles.get(pk=article_id)
    article.delete()
    
    return redirect(reverse('index'),permanent=True)

def modifier(request,article_id):
    article=get_object_or_404(Article,pk=article_id)
    if request.method=='POST':
        form=ModifierArticle(request.POST,instance=article)
        if form.is_valid():
            form.save()
            return redirect(reverse('index'),permanent=True)
    else:
        form=ModifierArticle(instance=article)
        return render(request,'modifier.html',locals())

def afficher(request,article_id):
    article=Article.objects.all().get(pk=article_id)
    return render(request,'afficher.html',locals())