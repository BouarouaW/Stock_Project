# forms.py
from django import forms
from .models import Client
from .models import Commande

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['nom', 'prenom', 'email', 'telephone', 'adresse']





class CommandeForm(forms.ModelForm):
    class Meta:
        model = Commande
        fields = ['client', 'produit', 'date', 'quantite']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})
        }

    def clean_quantite(self):
        quantite = self.cleaned_data['quantite']
        produit = self.cleaned_data['produit']
        if quantite > produit.quantite:
            raise forms.ValidationError("La quantité demandée est supérieure à la quantité disponible.")
        return quantite
