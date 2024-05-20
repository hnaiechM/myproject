from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Poste
from .models import Stage

def home(request):
  postes = Poste.objects.all()
  context = {"postes" : postes}
  return render(request, "home.html", context)

def detail(request, id):
    postes = get_object_or_404(Poste, id=id)
    postes_en_relation = Poste.objects.filter(type=postes.type).exclude(id=postes.id)
    return render(request, 'detail.html', {"postes": postes, "postes_en_relation": postes_en_relation})

def search(request):
  query=request.GET["poste"]
  liste_poste=Poste.objects.filter(type=query)
  return render(request, "search.html",{"liste_poste":liste_poste})

def stage(request, id):
  stage = Stage.objects.all()
  liste_stage = {"stage": stage}
  return render(request, "stage.html", {"liste_stage" : liste_stage})

def contact(request):
  return render(request, "contact.html")