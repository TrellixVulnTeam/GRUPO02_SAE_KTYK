# Generated by Django 2.2.5 on 2019-10-26 03:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Registro', '0007_auto_20191017_1348'),
        ('quiz', '0002_auto_20190914_1551'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='asignatura',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Registro.Asignatura'),
        ),
    ]
