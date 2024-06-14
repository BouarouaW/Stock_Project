# employe_panel/forms.py
from django import forms
from .models import Fournisseur

class FournisseurForm(forms.ModelForm):
    class Meta:
        model = Fournisseur
        fields = ['nom', 'prenom', 'email', 'telephone']



from .models import Categorie

class CategorieForm(forms.ModelForm):
    class Meta:
        model = Categorie
        fields = ['title', 'fournisseur']

from django import forms
from .models import Produit, Categorie

class ProduitForm(forms.ModelForm):
    categorie = forms.ModelChoiceField(queryset=Categorie.objects.all())

    class Meta:
        model = Produit
        fields = ['nom', 'description', 'prix', 'quantite', 'categorie']




from django import forms
from .models import Produit

class ProduitModificationForm(forms.ModelForm):
    class Meta:
        model = Produit
        fields = ['nom', 'description', 'prix', 'quantite', 'categorie']
