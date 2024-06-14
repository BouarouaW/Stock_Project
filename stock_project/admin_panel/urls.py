from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('categories/', views.liste_categories, name='liste_categories'),
    path('fournisseurs/', views.liste_fournisseurs, name='liste_fournisseurs'),
    path('ajouter-fournisseur/', views.ajouter_fournisseur, name='ajouter_fournisseur'),
    path('supprimer-fournisseur/<int:fournisseur_id>/', views.supprimer_fournisseur, name='supprimer_fournisseur'),
    path('ajouter-categorie/', views.ajouter_categorie, name='ajouter_categorie'),
    path('supprimer-categorie/<int:categorie_id>/', views.supprimer_categorie, name='supprimer_categorie'),
    path('ajouter-produit/', views.ajouter_produit, name='ajouter_produit'),
    path('detail-produit/<int:produit_id>/', views.detail_produit, name='detail_produit'),
    path('liste-produits/', views.liste_produits, name='liste_produits'),
    path('supprimer-produit/<int:produit_id>/', views.supprimer_produit, name='supprimer_produit'),
    path('modifier-produit/<int:produit_id>/', views.modifier_produit, name='modifier_produit'),
    path('gerer-stock/', views.gerer_stock, name='gerer_stock'),
    path('reapprovisionnement-stock/', views.reapprovisionnement_stock, name='reapprovisionnement_stock'),
    path('historique-approvisionnement/', views.historique_approvisionnement, name='historique_approvisionnement'),

]

