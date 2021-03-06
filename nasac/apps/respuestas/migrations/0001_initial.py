# Generated by Django 3.0 on 2021-08-21 21:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('preguntas', '0002_auto_20210821_1824'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Respuesta',
            fields=[
                ('timemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.TimeModel')),
                ('nombre', models.CharField(max_length=100)),
                ('puntaje', models.IntegerField(default=0)),
                ('preguntas', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='preguntas.Pregunta')),
            ],
            bases=('core.timemodel',),
        ),
    ]
