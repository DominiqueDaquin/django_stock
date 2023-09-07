from tempfile import NamedTemporaryFile
from django.shortcuts import render
from gestion.models import Article
from .models import Pannier,Compte
from .forms import InscriptionForm,AjouterPannierForm,ConnexionForm
from django.shortcuts import redirect
from django.urls import reverse
from django.http import HttpResponse
from django.http import FileResponse
from django.template.loader import render_to_string
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import pdfkit
def index(request):
    connexion=False
    if request.method=='POST':
        form=InscriptionForm(request.POST,request.FILES)
        if form.is_valid():
            article=form.save()
            request.session['compte_id']=article.id
            print('valide')
            print(request.session.get('compte_id'))
            return redirect(reverse('clientpage:accueil'),permanent=True)
    else:
        form=InscriptionForm()
    
    return render(request,'index2.html',locals())

def accueil(request):
    articles=Article.objects.all()
    return render(request,'accueil.html',locals())

def ajouter_pannier(request,article_id):
    article=Article.objects.all().get(pk=article_id)
    compte_id=request.session.get('compte_id')
    compte=Compte.objects.all().get(pk=compte_id)
    if request.method=='POST':
        form=AjouterPannierForm(request.POST)
       
        if form.is_valid():
            quantite=form.cleaned_data['quantite']
            nouveau=Pannier()
            nouveau.articleid=article
            nouveau.quantite=quantite
            nouveau.compte=compte
            nouveau.save()
            return redirect(reverse('clientpage:pannier'),permanent=True)
            
            

    else:
        form=AjouterPannierForm()
    return render(request,'ajouter-pannier.html',locals())

def connexion(request):
    connexion=True
    if request.method=='POST':
        form=ConnexionForm(request.POST)
        if form.is_valid():
            nom=form.nom
            mdp=form.mdp
            print(nom)
            compte=Compte.objects.all().get(nom=nom)
            print(compte)
            return redirect(reverse('clientpage:accueil'),permanent=True)
    else:
        form=ConnexionForm()
    return render(request,'index2.html',locals())
        
def supprimer_pannier(request,id_article):
    compte_id=request.session.get('compte_id')
    compte=Compte.objects.all().get(pk=compte_id)
    pannierclient=Pannier.objects.filter(compte=compte)
    item=pannierclient.get(pk=id_article)
    item.delete()
    return render(request,'pannier.html',locals())
    
def facture(request,itemid):    
    
    reponse=HttpResponse(content_type='application/pdf')
    reponse['Content-Disposition']='facture.pdf'
    p=canvas.Canvas(reponse,pagesize=letter)
    
    p.showPage()
    p.save()
    return reponse

def facturation(request,file):
    
   
    config=pdfkit.configuration(wkhtmltopdf=r'/usr/bin/wkhtmltopdf')
    html = str(file.content, 'utf-8')
    with NamedTemporaryFile(delete=False, suffix='.html') as temp_html:
            temp_html.write(html.encode('utf-8'))
    try:

        print(temp_html.name)
        pdf=pdfkit.from_file(temp_html.name,False,configuration=config)
        response=HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition']='attachment; filename="file_name.pdf"'
        print('yyyu')
        return response        
    except Exception as e:
        
        
        
        return HttpResponse(f'Erreur lors du tele chargement de la facture {e}')
        

    
        
def pannier(request):
    try:
        compte_id=request.session.get('compte_id')
        print(compte_id)
        compte=Compte.objects.all().get(pk=compte_id)
        pannierclient=Pannier.objects.filter(compte=compte)
    except Exception as e:
        print(e)
    return render(request,'pannier.html',locals())



def acheter(request):
    if request.method=='POST':
        download=request.POST.get('telecharger')

        print(download)
        ligne=request.POST.getlist('ligne')
        lignes=list(map(int,ligne))
        compte_id=request.session.get('compte_id')
        compte=Compte.objects.all().get(pk=compte_id)
        pannierclient=Pannier.objects.filter(compte=compte)
        ligne_selectionne=[]
        somme=0
        for ligne in lignes:
            
            l=pannierclient.get(pk=ligne)
            p=l.articleid.prix*l.quantite
            somme +=p
            print(l.articleid.nom)
            ligne_selectionne.append(l)
        if download is not None:
            return facturation(request,render(request,'facture.html',locals()))
       
        return render(request,'facture.html',locals())
    return redirect('clientpage:pannier')