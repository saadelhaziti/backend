from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from .models import Student,verfeed,modules


# Create your views here.
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt


def logine(request):
    if request.method == 'GET':
         return render(request , 'index.html')
    
    data = json.loads(request.body)

    try:
        user = verfeed.objects.get(email=data['email'])
        if user.password == data['password'] :
            moduls = modules.objects.all()
            module_data = {f'module {i+1}': module.title for i, module in enumerate(moduls)}
            

            return JsonResponse({'name': user.nom,'prenom': user.prenom,
                                'cne': user.cne,'cni': user.cni,
                                'email': user.email,
                                'date_naissance': user.date_naissance,'adresse': user.adresse,
                                'specialite_bac': user.specialite_bac,'annee_obtention_bac': user.annee_obtention_bac,
                                'mention_bac': user.mention_bac,'diplome_obtenu': user.diplome_obtenu,
                                'specialite_diplome': user.specialite_diplome,'annee_obtention_diplome': user.annee_obtention_diplome,
                                'mention_diplome': user.mention_diplome,
                                'prof': user.prof,'authenticated': user.verfed,
                                'modules': module_data})
        else :
            return JsonResponse({'authenticated': False})
    except Student.DoesNotExist:
        return JsonResponse({'authenticated': False})

@csrf_exempt
def register(request):
    if request.method == 'GET':
        return render(request , 'index.html')
    data = json.loads(request.body)

    
    user= Student()
    user.nom =data['name']
    user.prenom =data['prenom']
    user.cne =data['cne']
    user.cni =data['cni']
    user.email =data['email']
    user.password =data['password']
    user.date_naissance =data['dateNaissance']
    user.adresse =data['adresse']
    user.specialite_bac =data['specialiteBac']
    user.annee_obtention_bac =data['anneeObtentionBac']
    user.mention_bac =data['mentionBac']
    user.diplome_obtenu =data['diplomeObtenu']
    user.specialite_diplome =data['specialiteDiplome']
    user.annee_obtention_diplome =data['anneeObtentionDiplome']
    user.mention_diplome =data['mentionDiplome']
    user.save()
    return JsonResponse({'authenticated': True})

def user(request):
    
    return render(request , 'index.html')


def index(request):
    return render(request , 'index.html')