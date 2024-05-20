from django import forms
from django.contrib.auth.models import User
from . import models
#peut hérite de forms.Form ou  forms.ModelForm
class PostForm(forms.ModelForm):
  class Meta:
    model = models.Poste
    fields = ['type', 'date', 'user', 'image']

class ReactionForm(forms.ModelForm):
  class Meta:
    model = models.Reaction
    fields = "__all__"

class EvenementForm(forms.ModelForm):
  class Meta:
    model = models.Evenement
    fields = "__all__"

class StudentUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
  