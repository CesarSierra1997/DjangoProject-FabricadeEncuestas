# Generated by Django 4.2.2 on 2024-10-07 01:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('encuesta', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='respuestaencuestaprivada',
            name='usuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='usuario_encuesta', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='respuesta',
            name='pregunta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='respuestas', to='encuesta.pregunta'),
        ),
        migrations.AddField(
            model_name='respuesta',
            name='respuestaEncuestaPrivada',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='respuestas_privadas', to='encuesta.respuestaencuestaprivada'),
        ),
        migrations.AddField(
            model_name='respuesta',
            name='respuestaEncuestaPublica',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='respuestas_publicas', to='encuesta.respuestaencuestapublica'),
        ),
        migrations.AddField(
            model_name='pregunta',
            name='encuesta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='encuesta.encuesta'),
        ),
        migrations.AddField(
            model_name='opcionespregunta',
            name='pregunta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='opciones', to='encuesta.pregunta'),
        ),
        migrations.AddField(
            model_name='encuesta',
            name='administrador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='respuestaencuestapublica',
            unique_together={('encuesta', 'numeroDocumento', 'email')},
        ),
    ]
