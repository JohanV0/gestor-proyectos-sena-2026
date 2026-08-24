from django.db import models

class Proyecto(models.Model):
    '''
    Modelo que representa un proyecto
    '''
    nombre = models.CharField(max_length=100) #Campo de texto (varchar)
    descripcion = models.TextField() #texto largo
    duracion = models.IntegerField() #entero


class Tarea(models.Model):
    '''
    modelo que representa la tarea de un proyecto
    '''

    PRIORIDAD_CHOICES = [
        ('BAJA', 'baja'),
        ('MEDIA','media'),
        ('ALTA','alta'),
    ]
    ESTADO_CHOICES = [
        ('PENDIENTE','pendiente'),
        ('EN_PROGRESO','en_progreso'),
        ('COMPLETADA','completada'),
    ]
    
    # relacion 1 a muchos: un proyecto tiene muchas tareas
    proyecto = models.ForeignKey(
        Proyecto,
        on_delete = models.CASCADE,
        related_name='tareas',
    )
    titulo = models.CharField(max_length=50)
    prioridad = models.CharField(
        max_length=5,
        choices= PRIORIDAD_CHOICES,
        default='MEDIA')
    estado = models.CharField(
        max_length=11,
        choices= ESTADO_CHOICES,
        default='PENDIENTE'
    )