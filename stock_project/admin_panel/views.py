from django.shortcuts import render, redirect
from .models import Fournisseur, Categorie
from .forms import FournisseurForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import Fournisseur
from .forms import CategorieForm
from .models import Categorie
from .forms import ProduitForm
from .models import Produit
from .forms import ProduitModificationForm
from .models import ApprovisionnementHistorique


def admin_dashboard(request):
    return render(request, 'admin_panel/dashboard.html')


def liste_categories(request):
    categories = Categorie.objects.all()
    return render(request, 'admin_panel/liste_categories.html', {'categories': categories})

def liste_fournisseurs(request):
    fournisseurs = Fournisseur.objects.all()
    return render(request, 'admin_panel/liste_fournisseurs.html', {'fournisseurs': fournisseurs})


def ajouter_fournisseur(request):
    if request.method == 'POST':
        form = FournisseurForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_fournisseurs')
    else:
        form = FournisseurForm()
    return render(request, 'admin_panel/ajouter_fournisseur.html', {'form': form})




def supprimer_fournisseur(request, fournisseur_id):
    fournisseur = get_object_or_404(Fournisseur, pk=fournisseur_id)
    fournisseur.delete()
    return redirect('liste_fournisseurs')



def ajouter_categorie(request):
    if request.method == 'POST':
        form = CategorieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_categories')
    else:
        form = CategorieForm()
    return render(request, 'admin_panel/ajouter_categorie.html', {'form': form})



def supprimer_categorie(request, categorie_id):
    categorie = get_object_or_404(Categorie, pk=categorie_id)
    if request.method == 'POST':
        categorie.delete()
        return redirect('liste_categories') 
    return render(request, 'admin_panel/supprimer_categorie.html', {'categorie': categorie})




def ajouter_produit(request):
    if request.method == 'POST':
        form = ProduitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_produits')
    else:
        form = ProduitForm()
    return render(request, 'admin_panel/ajouter_produit.html', {'form': form})





def detail_produit(request, produit_id):
    produit = get_object_or_404(Produit, pk=produit_id)
    return render(request, 'admin_panel/detail_produit.html', {'produit': produit})


def liste_produits(request):
    produits = Produit.objects.all()
    return render(request, 'admin_panel/liste_produits.html', {'produits': produits})



def supprimer_produit(request, produit_id):
    produit = get_object_or_404(Produit, pk=produit_id)
    produit.delete()
    return redirect('liste_produits')




def modifier_produit(request, produit_id):
    produit = get_object_or_404(Produit, pk=produit_id)
    if request.method == 'POST':
        form = ProduitModificationForm(request.POST, instance=produit)
        if form.is_valid():
            form.save()
            return redirect('detail_produit', produit_id=produit_id)
    else:
        form = ProduitModificationForm(instance=produit)
    return render(request, 'admin_panel/modifier_produit.html', {'form': form})



def gerer_stock(request):
    produits = Produit.objects.all()
    return render(request, 'admin_panel/gerer_stock.html', {'produits': produits})



def reapprovisionnement_stock(request):
    if request.method == 'POST':
        for key, value in request.POST.items():
            if key.startswith('quantite_'):
                produit_id = int(key.split('_')[1])
                quantite = int(value)
                produit = Produit.objects.get(pk=produit_id)
                produit.quantite += quantite
                produit.save()
                approvisionnement_historique = ApprovisionnementHistorique(
                    produit=produit,
                    quantite_ajoutee=quantite
                )
                approvisionnement_historique.save()
        return redirect('gerer_stock')
    else:
        produits = Produit.objects.all()
        return render(request, 'admin_panel/reapprovisionnement_stock.html', {'produits': produits})


def historique_approvisionnement(request):
    historique = ApprovisionnementHistorique.objects.all()
    return render(request, 'admin_panel/historique_approvisionnement.html', {'historique': historique})
