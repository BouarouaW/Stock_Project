# models.py
from django.db import models

from admin_panel.models import Produit

class Client(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telephone = models.CharField(max_length=15)
    adresse = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.prenom} {self.nom}"


class Commande(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    date = models.DateField()
    quantite = models.IntegerField()

    def __str__(self):
        return f"Commande {self.id} - {self.client.nom} - {self.produit.nom}"
    


class Facture(models.Model):
    commande = models.OneToOneField(Commande, on_delete=models.CASCADE)
    contenu_html = models.TextField()