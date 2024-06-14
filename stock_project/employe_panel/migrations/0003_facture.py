# Generated by Django 5.0.4 on 2024-04-13 15:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employe_panel', '0002_commande'),
    ]

    operations = [
        migrations.CreateModel(
            name='Facture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenu_html', models.TextField()),
                ('commande', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='employe_panel.commande')),
            ],
        ),
    ]