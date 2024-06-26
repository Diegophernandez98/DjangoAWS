from django.db import models
from django.utils import timezone

class Rol(models.Model):
    nombre = models.CharField(max_length=20, null=False)

class Usuario(models.Model):
    rut = models.CharField(max_length=12, unique=True, null=False)
    nombre = models.CharField(max_length=50, null=False)
    apellido = models.CharField(max_length=50, null=False)
    correo = models.CharField(max_length=100, null=False)
    numero = models.CharField(max_length=15, null=False)
    comuna = models.CharField(max_length=20, null=False)
    direccion = models.CharField(max_length=100, null=False)
    contrasena = models.CharField(max_length=50, default='123', null=False)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE, null=False, blank=True, default=9999999)
    fecha_ingreso = models.DateField(null=False)

class Plan_Internet(models.Model):
    nombre = models.CharField(max_length=50, null=False)
    descripcion = models.CharField(max_length=255, default='default')
    valor_mensual = models.IntegerField(null=False)
    adicional = models.CharField(max_length=50, null=False, default='default')
    instalacion = models.IntegerField(null=False)
    extensor = models.CharField(max_length=50, null=False, default='default')

class Plan_Television(models.Model):
    nombre = models.CharField(max_length=50, null=False)
    descripcion = models.CharField(max_length=255, default='default')
    valor_mensual = models.IntegerField(null=False)
    adicional = models.CharField(max_length=50, null=False, default='default')
    Asistencia = models.CharField(max_length=50, null=False, default='default')
    extras = models.CharField(max_length=50, null=False, default='default')


class Plan_Telefonia(models.Model):
    nombre = models.CharField(max_length=50, null=False)
    descripcion = models.CharField(max_length=255, default='default')
    valor_mensual = models.IntegerField(null=False)
    adicional = models.CharField(max_length=50, null=False, default='default')
    extras = models.CharField(max_length=50, null=False, default='default')
    roaming = models.CharField(max_length=50, null=False, default='default')

class Tipo_Plan(models.Model):
    telefonia = models.ForeignKey(Plan_Telefonia, on_delete=models.CASCADE, null=False)
    internet = models.ForeignKey(Plan_Internet, on_delete=models.CASCADE, null=False)
    television = models.ForeignKey(Plan_Television, on_delete=models.CASCADE, null=False)


class Descuento(models.Model):
    nombre = models.IntegerField(null=False)

class Boleta(models.Model):
    cliente = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=False, default=9999999)
    fecha_emision = models.DateField(null=False)
    fecha_vencimiento = models.DateField(null=False)
    detalles = models.CharField(max_length=255, null=False)
    valor = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    valor_con_descuento = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=9999999)
    descuento = models.ForeignKey(Descuento, on_delete=models.CASCADE, null=False, default=9999999)
    plan_telefonia = models.ForeignKey(Plan_Telefonia, on_delete=models.CASCADE, null=True)
    plan_television = models.ForeignKey(Plan_Television, on_delete=models.CASCADE, null=True)
    plan_internet = models.ForeignKey(Plan_Internet, on_delete=models.CASCADE, null=True)

class Comentario(models.Model):
    cliente = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=False)
    texto = models.TextField(null=False)
    fecha = models.DateField(null=False)