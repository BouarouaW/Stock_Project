from django.urls import path
from . import views
app_name = 'employe_panel' 
urlpatterns = [
    path('dashboard/', views.employe_dashboard, name='employe_dashboard'),
    path('inscription-client/', views.inscription_client, name='inscription_client'),
    path('ajouter-commande/', views.ajouter_commande, name='ajouter_commande'),
    path('command-history/', views.command_history, name='command_history'),
    path('sales-trends/', views.sales_trends, name='sales_trends'),
    path('imprimer-facture/<int:commande_id>/', views.imprimer_facture, name='imprimer_facture'),


]
