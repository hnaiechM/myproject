# Generated by Django 5.0.6 on 2024-05-16 22:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Poste',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('date', models.DateField()),
                ('slug', models.SlugField(default='', max_length=200, unique=True)),
                ('type', models.CharField(choices=[('evenement', 'Evenement'), ('stage', 'Stage'), ('logement', 'Logement'), ('transport', 'Transport'), ('recommandation', 'Recommandation')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('prenom', models.CharField(max_length=100)),
                ('telephone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Evenement',
            fields=[
                ('poste_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='student_app.poste')),
                ('intitule', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('lieu', models.CharField(max_length=255)),
                ('contactinfo', models.CharField(max_length=255)),
            ],
            bases=('student_app.poste', models.Model),
        ),
        migrations.CreateModel(
            name='Logement',
            fields=[
                ('poste_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='student_app.poste')),
                ('localisation', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('contact_info', models.CharField(max_length=255)),
            ],
            bases=('student_app.poste',),
        ),
        migrations.CreateModel(
            name='Recommandation',
            fields=[
                ('poste_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='student_app.poste')),
                ('text', models.CharField(max_length=255)),
            ],
            bases=('student_app.poste', models.Model),
        ),
        migrations.CreateModel(
            name='Stage',
            fields=[
                ('poste_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='student_app.poste')),
                ('type_stg', models.IntegerField()),
                ('societe', models.CharField(max_length=255)),
                ('duree', models.IntegerField()),
                ('sujet', models.CharField(max_length=255)),
                ('contact_info', models.CharField(max_length=255)),
                ('specialite', models.CharField(max_length=255)),
            ],
            bases=('student_app.poste', models.Model),
        ),
        migrations.CreateModel(
            name='Transport',
            fields=[
                ('poste_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='student_app.poste')),
                ('depart', models.CharField(max_length=255)),
                ('destination', models.CharField(max_length=255)),
                ('heure_dep', models.TimeField()),
                ('nbre_places', models.IntegerField()),
                ('contact_info', models.CharField(max_length=255)),
            ],
            bases=('student_app.poste', models.Model),
        ),
        migrations.CreateModel(
            name='Reaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('like', models.BooleanField()),
                ('Post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student_app.poste')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student_app.user')),
            ],
        ),
        migrations.AddField(
            model_name='poste',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student_app.user'),
        ),
        migrations.CreateModel(
            name='EvenClub',
            fields=[
                ('evenement_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='student_app.evenement')),
                ('club', models.CharField(max_length=255)),
            ],
            bases=('student_app.evenement', models.Model),
        ),
        migrations.CreateModel(
            name='EvenSocial',
            fields=[
                ('evenement_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='student_app.evenement')),
                ('prix', models.FloatField()),
            ],
            bases=('student_app.evenement', models.Model),
        ),
    ]
