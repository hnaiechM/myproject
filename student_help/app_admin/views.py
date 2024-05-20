from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView, CreateView,DeleteView
from django.http import HttpResponse
from student_app.models import Poste
from django.contrib.auth.models import User
from student_app.forms import PostForm
from django import forms
# Create your views here.
def dashboard(request):
  return render(request, 'db.html')
def user_postes(request):
  if not request.user.is_authenticated:
    return render('home')
    postes = Poste.objects.all()
  else:
    list_postes = Poste.objects.filter(user=request.user)
    return render (request,'my_postes.html',{'list_postes':list_postes})
def add_poste(request):
  if request.method == 'POST':
     form = PostForm(request.POST, request.FILES)
  else:
        form = PostForm()
  return render(request, 'add-poste.html', {'form': form})

class UpdatePoste(UpdateView):
    model = Poste
    template_name = 'poste_form.html'
    fields = ['type', 'date', 'user', 'image']
    success_url = reverse_lazy('my_postes')  # Redirect to the list view

class DeletePoste(DeleteView):
  model = Poste
  success_url = reverse_lazy('my_postes')
  template_name = 'app_stud/poste_confirm_delete.html'