# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-08 21:46
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Elu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(db_index=True, max_length=255)),
                ('family_name', models.CharField(db_index=True, max_length=255)),
                ('gender', models.CharField(blank=True, choices=[('H', 'Homme'), ('F', 'Femme'), ('', 'Inconnu')], max_length=1)),
                ('birthdate', models.DateField(blank=True, null=True)),
                ('role', models.CharField(choices=[('M', 'Maire'), ('CD', 'Conseiller départemental'), ('CR', 'Conseiller régional'), ('D', 'Député')], max_length=2)),
                ('comment', models.TextField(blank=True)),
                ('priority', models.IntegerField(default=500)),
                ('public_email', models.CharField(blank=True, max_length=255)),
                ('public_phone', models.CharField(blank=True, max_length=255)),
                ('public_website', models.URLField(blank=True, max_length=255)),
                ('private_email', models.CharField(blank=True, max_length=255)),
                ('private_phone', models.CharField(blank=True, max_length=255)),
                ('status', models.IntegerField(choices=[(1, "Rien n'a été fait"), (2, 'Élu contacté'), (3, 'Élu doit être recontacté'), (10, 'Parrainage refusé'), (20, 'Parrainage accepté')], db_index=True, default=1)),
                ('department', models.CharField(blank=True, db_index=True, max_length=3)),
                ('city', models.CharField(blank=True, db_index=True, max_length=255)),
                ('city_size', models.IntegerField(blank=True, null=True)),
                ('nuance_politique', models.CharField(blank=True, db_index=True, max_length=5)),
                ('assigned_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('note', models.TextField()),
                ('elu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Elu')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
