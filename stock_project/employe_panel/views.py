from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Commande
from collections import Counter
from django.db.models import Sum  
from .forms import CommandeForm
from .forms import ClientForm
from django.template.loader import get_template
from xhtml2pdf import pisa
from .models import Facture


def employe_dashboard(request):
    return render(request, 'employe_panel/dashboard.html')



def inscription_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employe_panel:ajouter_commande') 
    else:
        form = ClientForm()
    return render(request, 'employe_panel/inscription_client.html', {'form': form})



def ajouter_commande(request):
    if request.method == 'POST':
        form = CommandeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employe_panel:command_history')  
    else:
        form = CommandeForm()
    return render(request, 'employe_panel/ajouter_commande.html', {'form': form})


def command_history(request):
    commandes = Commande.objects.all()
    return render(request, 'employe_panel/command_history.html', {'commandes': commandes})




def sales_trends(request):
    commandes = Commande.objects.all()
    
    product_sales = Counter()
    for commande in commandes:
        product_sales[commande.produit.nom] += commande.quantite
    
    sorted_products = sorted(product_sales.items(), key=lambda x: x[1], reverse=True)
    
    return render(request, 'employe_panel/sales_trends.html', {'product_sales': sorted_products})


def imprimer_facture(request, commande_id):
    commande = Commande.objects.get(pk=commande_id)
    template_path = 'employe_panel/facture_template.html'
    context = {'commande': commande}
    template = get_template(template_path)
    html = template.render(context)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="facture.pdf"'
    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('Une erreur s\'est produite lors de la génération du PDF')
    else:
        facture = Facture(commande=commande, contenu_html=html)
        facture.save()
        return response