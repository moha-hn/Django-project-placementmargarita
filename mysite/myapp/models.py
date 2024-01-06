from django.db import models
from django.utils import timezone
# Create your models here.
class job(models.Model):
    titre=models.CharField(max_length=20)
    description=models.CharField(max_length=300,blank=True)
    prix=models.FloatField(max_length=10,blank=True)
    employeur=models.CharField(max_length=50,blank=True)
    horaire=models.CharField(max_length=50,blank=True)
    date=models.DateField(auto_now_add=True,editable=False)
    def __str__(self):
        return self.titre
    

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name
    

class candidat(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email=models.EmailField()
    job = models.ForeignKey(job,on_delete=models.CASCADE)
    cv=models.FileField(blank=True)

    def __str__(self):
        return self.nom