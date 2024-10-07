from django.db import models
from django.core.exceptions import ValidationError
from apps.usuario.models import Usuario


# ENCUESTA
class Encuesta(models.Model):
    titulo = models.CharField('Título', max_length=50, blank=False, null=False)
    TIPO_ENCUESTA = [
        ('Publica', 'Encuesta pública'),
        ('Privada', 'Encuesta privada'),
    ]
    tipoEncuesta = models.CharField('Tipo de Encuesta', max_length=50, choices=TIPO_ENCUESTA)
    administrador = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fechaInicio = models.DateTimeField(null=False)
    fechaFinal = models.DateTimeField(null=True)
    fechaCreacion = models.DateTimeField('Fecha de creación',auto_now_add=True)
    fechaModificacion = models.DateTimeField(auto_now_add=False, null=True)
    estado = models.BooleanField('Estado', default=True)
    publicarEncuesta = models.BooleanField('Visibilidad', default=False)
    fechaPublicacion = models.DateTimeField(auto_now_add=True)


    def __str__ (self):
        return f'{self.titulo} - tipo {self.tipoEncuesta}'
    
    class Meta:
        verbose_name_plural = 'Encuestas'
        ordering = ['-id']
        verbose_name = 'Encuesta'

# PREGUNTA
class Pregunta(models.Model):
    TIPO_PREGUNTA_CHOICES = [
        ('1', 'General'),
        ('2', 'Sí o no'),
        ('3', 'Numérica'),
        ('4', 'Selección múltiple'),
    ]
    tipoPregunta = models.CharField('Tipo de pregunta', max_length=30, choices=TIPO_PREGUNTA_CHOICES)
    texto_pregunta = models.CharField('Pregunta', max_length=200, blank=False, null=False)
    encuesta = models.ForeignKey(Encuesta, on_delete=models.CASCADE)

    def __str__(self):
        return self.texto_pregunta

# OPCION DE PREGUNTA
class OpcionesPregunta(models.Model):
    opcion_1 = models.CharField('Opción 1', max_length=50, blank=False, null=False)
    opcion_2 = models.CharField('Opción 2', max_length=50, blank=False, null=False)
    opcion_3 = models.CharField('Opción 3', max_length=50, blank=False, null=False)
    opcion_4 = models.CharField('Opción 4', max_length=50, blank=False, null=False)
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE, related_name="opciones")

    def __str__(self):
        return f"Opciones para la pregunta: {self.pregunta.texto_pregunta}"


# RESPUESTA ENCUESTA PÚBLICA
class RespuestaEncuestaPublica(models.Model):
    TIPO_USUARIO_CHOICES = [
        ('1', 'Ciudadano'),
        ('2', 'Aprendiz'),
        ('3', 'Estudiante'),
        ('4', 'Profecional'),
        ('5', 'Area administrativa'),
        ('6', 'Area de servicios'),
        ('7', 'Area de seguridad'),
        ('8', 'Sena'),
        ('9', 'Otros'),
    ]
    tipoUsuario = models.CharField('Tipo de usuario', max_length=30, choices=TIPO_USUARIO_CHOICES)
    TIPO_DOCUMENTO_CHOICES = [
        ('CC', 'Cédula de Ciudadanía'),
        ('TI', 'Tarjeta de Identidad'),
        ('PASAPORTE', 'Pasaporte'),
        ('REGISTRO_CIVIL', 'Registro civil'),
    ]
    tipoDocumento = models.CharField('Tipo de Documento', max_length=20, choices=TIPO_DOCUMENTO_CHOICES)
    numeroDocumento = models.CharField('Número de documento', max_length=12,blank=False, null=False, unique=True)
    nombre = models.CharField('Nombre completo', max_length=50, blank=False, null=False)
    email = models.EmailField('Correo Electrónico', max_length=254, blank=False, null=False, unique=True)
    encuesta = models.ForeignKey(Encuesta, on_delete=models.CASCADE, related_name='encuesta_preguntas_publica')

    class Meta:
        unique_together = ('encuesta', 'numeroDocumento', 'email')

# RESPUESTA ENCUESTA PRIVADA
class RespuestaEncuestaPrivada(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, related_name='usuario_encuesta')
    encuesta = models.ForeignKey(Encuesta, on_delete=models.CASCADE, related_name='encuesta_preguntas_privada')

# RESPUESTA A PREGUNTAS
class Respuesta(models.Model):
    texto_respuesta = models.CharField('Digite su respuesta', max_length=200, blank=False, null=False)
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE, related_name='respuestas')
    respuestaEncuestaPublica = models.ForeignKey(RespuestaEncuestaPublica, on_delete=models.CASCADE, related_name='respuestas_publicas', null=True, blank=True)
    respuestaEncuestaPrivada = models.ForeignKey(RespuestaEncuestaPrivada, on_delete=models.CASCADE, related_name='respuestas_privadas', null=True, blank=True)
    fechaRespuesta = models.DateTimeField(auto_now_add=True)

    def clean(self):
        """Valida que una respuesta pertenezca solo a una encuesta pública o privada."""
        if self.respuestaEncuestaPublica and self.respuestaEncuestaPrivada:
            raise ValidationError("Una respuesta solo puede estar vinculada a una encuesta pública o privada, no a ambas.")
