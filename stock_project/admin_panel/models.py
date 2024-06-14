from django.db import models

class Fournisseur(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField()
    telephone = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nom} {self.prenom}"

class Categorie(models.Model):
    title = models.CharField(max_length=100)
    fournisseur = models.ForeignKey(Fournisseur, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    


class Produit(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    quantite = models.PositiveIntegerField(default=0)  
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom




class ApprovisionnementHistorique(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantite_ajoutee = models.IntegerField()
    date_approvisionnement = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.produit.nom} - {self.quantite_ajoutee}"
