# Generated by Django 3.0 on 2021-08-21 21:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('preguntas', '0002_auto_20210821_1824'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pregunta',
            old_name='categoria',
            new_name='categorias',
        ),
    ]
