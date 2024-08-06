from django.db import models
from django.core.exceptions import ValidationError


class Vehiculo(models.Model):
    patente = models.CharField(max_length=6, primary_key=True)
    marca = models.CharField(max_length=20, null=False)
    modelo = models.CharField(max_length=20, null=False)
    activo = models.BooleanField(default=False)
    year = models.IntegerField()

    def clean(self):
        if len(self.patente) > 6 or len(self.patente) < 6:
            raise ValidationError(
                "patente no válida, la patente debe tener una longitud exacta de 6 caracteres"
            )

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"[{self.patente}] {self.marca} {self.modelo}"


class Chofer(models.Model):
    rut = models.CharField(max_length=9, primary_key=True)
    nombre = models.CharField(max_length=50, null=False)
    apellido = models.CharField(max_length=50, null=False)
    activo = models.BooleanField(default=False)
    creacion_registro = models.DateField(auto_now=True)
    vehiculo = models.OneToOneField(Vehiculo, on_delete=models.CASCADE)


class RegistroContabilidad(models.Model):
    fecha_compra = models.DateField(null=False)
    valor = models.FloatField(null=False)
    vehiculo = models.OneToOneField(Vehiculo, on_delete=models.CASCADE)
