from django.urls import path
from .views import *
from .views import user_postes
from .views import add_poste
from .views import UpdatePoste
from .views import DeletePoste
#from .views import AddPoste
urlpatterns = [
  path('', dashboard, name="dashboard"),
  path('my_postes/', user_postes, name='my_postes'),
  path('add-poste/', add_poste, name='add-poste'),
#  path('add-poste/', AddPoste.as_view(), name='add-poste'),
  path('update-poste/<int:pk>', UpdatePoste.as_view(), name='update-poste'),
  path('delete-poste/<int:pk>', DeletePoste.as_view(), name='delete-poste'),
]