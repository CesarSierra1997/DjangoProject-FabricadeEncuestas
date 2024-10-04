# Generated by Django 4.2.2 on 2024-10-03 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('encuesta', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='respuestaencuestapublica',
            name='tipoUsuario',
            field=models.CharField(choices=[('1', 'Ciudadano'), ('2', 'Aprendiz'), ('3', 'Estudiante'), ('4', 'Profecional'), ('5', 'Area administrativa'), ('6', 'Area de servicios'), ('7', 'Area de seguridad'), ('8', 'Sena'), ('9', 'Otros')], default=1, max_length=30, verbose_name='Tipo de usuario'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='respuestaencuestapublica',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='Correo Electrónico'),
        ),
        migrations.AlterField(
            model_name='respuestaencuestapublica',
            name='numeroDocumento',
            field=models.CharField(max_length=12, unique=True, verbose_name='Digite su número de documento'),
        ),
    ]