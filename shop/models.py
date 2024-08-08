from django.db import models
#import model of django for user
from django.contrib.auth.models import User

class Client(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE) # null = true car on peut avoir un client qui n'as pas cree de compte donc il n'est pas un utilisateur de l'app
    name = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=200, null=True)
    
    def __str__(self):
        return self.nam
    
class Category(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.name    
# a product can be link to a categorie or not
        """
        MODEL.CASCADE means if i delete the user, de client will go to
        SET_NULL here he dont delete but he just field the field with null
        """
    
class Produit(models.Model):
    categorie = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    name = models.CharField(max_length=100, null=True)
    price = models.DecimalField(decimal_places=2,max_digits=10)
    digital = models.BooleanField(default=False, null=True, blank=True)
    image = models.ImageField(upload_to='shop', null=True, blank=True)
    date_ajout = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name    
    
class Commande(models.Model):
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, blank=True, null=True)
    date_commande = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=True)
    transaction_id = models.CharField(max_length=200, null=True)
    status = models.CharField(max_length=200, null=True, blank=True)
    total_trans = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    
    def __str__(self):
        return str(self.id)   
    
class CommandeArticle(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.SET_NULL, blank=True, null=True)
    commande = models.ForeignKey(Commande, on_delete=models.SET_NULL, blank=True, null=True)
    quantite = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)     
    
class AddressChipping(models.Model):
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, blank=True, null=True)
    commande = models.ForeignKey(Commande, on_delete=models.SET_NULL, blank=True, null=True)
    addresse = models.CharField(max_length=100, null=True)
    ville = models.CharField(max_length=100, null=True)
    zipcode = models.CharField(max_length=100, null=True)
    date_ajout = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.addresse    