# Generated by Django 5.0.6 on 2024-05-20 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_app', '0004_rename_user_studname_alter_poste_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poste',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]
