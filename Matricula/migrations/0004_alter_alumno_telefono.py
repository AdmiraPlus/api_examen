# Generated by Django 4.2.4 on 2023-09-07 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Matricula', '0003_alter_alumno_telefono'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='telefono',
            field=models.CharField(max_length=10),
        ),
    ]
