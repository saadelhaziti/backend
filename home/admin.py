from django.contrib import admin
from .models import Student,verfeed,modules

def veref(ModelAdmin, request, queryset):
    user = Student.objects.all()
    
    for student in user:
        if student.verfed == True :
            user_exists = verfeed.objects.filter(cni=student.cni, cne = student.cne).exists()
            if  user_exists == False:
                ver = verfeed()
                ver.nom = student.nom
                ver.prenom =student.prenom 
                ver.cne=student.cne 
                ver.cni =student.cni 
                ver.email =student.email 
                ver.password=student.password 
                ver.date_naissance =student.date_naissance 
                ver.adresse =student.adresse 
                ver.specialite_bac=student.specialite_bac
                ver.annee_obtention_bac=student.annee_obtention_bac 
                ver.mention_bac =student.mention_bac 
                ver.diplome_obtenu=student.diplome_obtenu 
                ver.specialite_diplome =student.specialite_diplome 
                ver.annee_obtention_diplome=student.annee_obtention_diplome 
                ver.mention_diplome =student.mention_diplome
                ver.verfed =student.verfed
                ver.save()
                student.delete()

           

class Studentadmin(admin.ModelAdmin):
    model = Student
    actions = [veref]

# Register your models here.
admin.site.register(Student,Studentadmin)
admin.site.register(modules)
admin.site.register(verfeed)


