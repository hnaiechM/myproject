from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User


class StudName(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    telephone = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return f"{self.prenom} {self.nom}"




class Poste(models.Model):
    image = models.ImageField(upload_to='media/', null=True, blank=True)
    type = models.IntegerField()
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE,null="True")
    slug = models.SlugField(max_length=200, unique=True, default='')
    #desc = models.CharField(max_length=255)
    POST_TYPES = [
        ('evenement', 'Evenement'),
        ('stage', 'Stage'),
        ('logement', 'Logement'),
        ('transport', 'Transport'),
        ('recommandation', 'Recommandation'),
    ]
    type = models.CharField(max_length=20, choices=POST_TYPES)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"poste-{self.id}-{self.type}-{self.date}")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Poste {self.id} - Type {self.type} - Date {self.date}"
class Reaction(models.Model):
    comment = models.TextField()
    like = models.BooleanField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Post = models.ForeignKey(Poste, on_delete=models.CASCADE)

    def __str__(self):
        reaction_type = 'Liked' if self.like else 'Disliked'
        return f"{reaction_type}: '{self.comment}' by {self.user} on {self.post}"
    
class Evenement(Poste,models.Model):
    intitule = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    lieu = models.CharField(max_length=255)
    contactinfo = models.CharField(max_length=255)

    def __str__(self):
        return super().__str__() + " " + self.intitule + " " + self.description + " " + self.lieu + " " + self.contactinfo

class Stage(Poste, models.Model):
    type_stg = models.IntegerField()
    societe = models.CharField(max_length=255)
    duree = models.IntegerField()
    sujet = models.CharField(max_length=255)
    contact_info = models.CharField(max_length=255)
    specialite = models.CharField(max_length=255)

    def __str__(self):
        return (
            str(self.type_stg) + " " +
            self.societe + " " +
            str(self.duree) + " " +
            self.specialite + " " +
            self.contact_info + " " +
            self.sujet
        )

    
class Logement(Poste):
    localisation = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    contact_info = models.CharField(max_length=255)

    def __str__(self):
        return self.localisation+self.description+self.contact_info



class Transport(Poste,models.Model):
    depart = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    heure_dep = models.TimeField()
    nbre_places = models.IntegerField()
    contact_info = models.CharField(max_length=255)

    def __str__(self):
        return f"Transport de {self.depart} à {self.destination}"


class EvenSocial(Evenement,models.Model):
    prix = models.FloatField()
    def __str__(self):
        return f"Social event by {self.club}"

class EvenClub(Evenement,models.Model):
    club = models.CharField(max_length=255)
    def __str__(self):
        return f"Social event by {self.club}"
class Recommandation(Poste,models.Model):
    text = models.CharField(max_length=255)
    def __str__(self):
        return f"Recommandation de {self.text}"

Poste.objects.all()
Poste.objects.filter()