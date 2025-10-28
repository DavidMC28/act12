from django.db import models

class Avion(models.Model):
    ESTADO_MANTENIMIENTO = [
        ('excelente', 'Excelente'),
        ('bueno', 'Bueno'),
        ('regular', 'Regular'),
        ('mantenimiento', 'En Mantenimiento'),
    ]
    
    id_avion = models.AutoField(primary_key=True)
    modelo_avion = models.CharField(max_length=255)
    capacidad_pasajeros = models.IntegerField()
    anio_fabricacion = models.IntegerField()
    estado_mantenimiento = models.CharField(
        max_length=20, 
        choices=ESTADO_MANTENIMIENTO, 
        default='bueno'
    )
    horas_vuelo = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    foto = models.ImageField(upload_to='aviones/', blank=True, null=True)  # ← NUEVO CAMPO

    def __str__(self):
        return f"{self.modelo_avion} - {self.id_avion}"

    class Meta:
        verbose_name = "Avión"
        verbose_name_plural = "Aviones"
        ordering = ['modelo_avion']

class Vuelo(models.Model):
    id_vuelo = models.AutoField(primary_key=True)
    numero_vuelo = models.CharField(max_length=20, unique=True)
    origen = models.CharField(max_length=255)
    destino = models.CharField(max_length=255)
    id_avion = models.ForeignKey(
        Avion, 
        on_delete=models.CASCADE,
        related_name='vuelos'
    )
    fecha_hora_salida = models.DateTimeField()

    def __str__(self):
        return f"Vuelo {self.numero_vuelo} - {self.origen} a {self.destino}"

    class Meta:
        verbose_name = "Vuelo"
        verbose_name_plural = "Vuelos"
        ordering = ['-fecha_hora_salida']