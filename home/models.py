from django.db import models

class Encuesta(models.Model):
    nombre = models.CharField(max_length = 40)
    incremento = models.DecimalField(max_digits=4, decimal_places=2)
    numIteraciones = models.IntegerField()
    categoria = models.TextField()
    #marca= models.ManyToManyField(Marca)
    date = models.DateTimeField()

    def __str__(self):
        return self.nombre

class Marca(models.Model):
    nombre = models.CharField(max_length=40)
    precio = models.DecimalField(max_digits=4, decimal_places=2)
    imagen = models.ImageField()
    encuesta= models.ForeignKey(Encuesta, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre
