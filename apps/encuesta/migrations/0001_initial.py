# Generated by Django 4.2.2 on 2024-10-07 01:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Encuesta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50, verbose_name='Título')),
                ('tipoEncuesta', models.CharField(choices=[('Publica', 'Encuesta pública'), ('Privada', 'Encuesta privada')], max_length=50, verbose_name='Tipo de Encuesta')),
                ('fechaInicio', models.DateTimeField()),
                ('fechaFinal', models.DateTimeField(null=True)),
                ('fechaCreacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('fechaModificacion', models.DateTimeField(null=True)),
                ('estado', models.BooleanField(default=True, verbose_name='Estado')),
                ('publicarEncuesta', models.BooleanField(default=False, verbose_name='Visibilidad')),
                ('fechaPublicacion', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Encuesta',
                'verbose_name_plural': 'Encuestas',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='OpcionesPregunta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opcion_1', models.CharField(max_length=50, verbose_name='Opción 1')),
                ('opcion_2', models.CharField(max_length=50, verbose_name='Opción 2')),
                ('opcion_3', models.CharField(max_length=50, verbose_name='Opción 3')),
                ('opcion_4', models.CharField(max_length=50, verbose_name='Opción 4')),
            ],
        ),
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipoPregunta', models.CharField(choices=[('1', 'General'), ('2', 'Sí o no'), ('3', 'Numérica'), ('4', 'Selección múltiple')], max_length=30, verbose_name='Tipo de pregunta')),
                ('texto_pregunta', models.CharField(max_length=200, verbose_name='Pregunta')),
            ],
        ),
        migrations.CreateModel(
            name='Respuesta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto_respuesta', models.CharField(max_length=200, verbose_name='Digite su respuesta')),
                ('fechaRespuesta', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='RespuestaEncuestaPublica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipoUsuario', models.CharField(choices=[('1', 'Ciudadano'), ('2', 'Aprendiz'), ('3', 'Estudiante'), ('4', 'Profecional'), ('5', 'Area administrativa'), ('6', 'Area de servicios'), ('7', 'Area de seguridad'), ('8', 'Sena'), ('9', 'Otros')], max_length=30, verbose_name='Tipo de usuario')),
                ('tipoDocumento', models.CharField(choices=[('CC', 'Cédula de Ciudadanía'), ('TI', 'Tarjeta de Identidad'), ('PASAPORTE', 'Pasaporte'), ('REGISTRO_CIVIL', 'Registro civil')], max_length=20, verbose_name='Tipo de Documento')),
                ('numeroDocumento', models.CharField(max_length=12, unique=True, verbose_name='Número de documento')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre completo')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Correo Electrónico')),
                ('encuesta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='encuesta_preguntas_publica', to='encuesta.encuesta')),
            ],
        ),
        migrations.CreateModel(
            name='RespuestaEncuestaPrivada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('encuesta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='encuesta_preguntas_privada', to='encuesta.encuesta')),
            ],
        ),
    ]
