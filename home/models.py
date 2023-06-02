from django.db import models

# Create your models here.

class Student(models.Model):
    prenom = models.CharField(max_length=100)
    nom = models.CharField(max_length=100)
    cne = models.CharField(max_length=10)
    cni = models.CharField(max_length=12)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    date_naissance = models.DateField()
    adresse = models.CharField(max_length=200)
    specialite_bac = models.CharField(max_length=100)
    annee_obtention_bac = models.IntegerField()
    mention_bac = models.CharField(max_length=100)
    diplome_obtenu = models.CharField(max_length=100)
    specialite_diplome = models.CharField(max_length=100)
    annee_obtention_diplome = models.IntegerField()
    mention_diplome = models.CharField(max_length=100)
    verfed = models.BooleanField(default=False)


    def __str__(self):
        return self.nom





class verfeed(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    cne = models.CharField(max_length=10)
    cni = models.CharField(max_length=12)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    date_naissance = models.DateField()
    adresse = models.CharField(max_length=200,default=None)
    specialite_bac = models.CharField(max_length=100)
    annee_obtention_bac = models.IntegerField()
    mention_bac = models.CharField(max_length=100)
    diplome_obtenu = models.CharField(max_length=100)
    specialite_diplome = models.CharField(max_length=100)
    annee_obtention_diplome = models.IntegerField()
    mention_diplome = models.CharField(max_length=100)
    prof = models.BooleanField(default=False)
    verfed = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nom
    



class modules(models.Model):
    title = models.CharField(max_length=50)
    def __str__(self):
        return self.id

    
    class Meta:
        
        verbose_name = ("module")
        verbose_name_plural = ("modules")
