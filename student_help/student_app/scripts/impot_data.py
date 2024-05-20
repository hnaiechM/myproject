from student_app.models import Poste

def run():
  for i in range(1,20):
    postes = Poste()
    postes.id="Poste N° #%d" % i
    postes.slug="description poste N° #%d" % i
    postes.image="http://default"
    postes.date="date de le poste N° #%d" % i
    postes.save()
print("operation reussie")
