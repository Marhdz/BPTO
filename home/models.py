from django.db import models

class Encuesta(models.Model):
    nombre = models.CharField(max_length = 40)
    incremento = models.DecimalField(max_digits=4, decimal_places=2)
    numIteraciones = models.IntegerField()
    categoria = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.nombre

class Marca(models.Model):
    nombre = models.CharField(max_length=40)
    precio = models.DecimalField(max_digits=4, decimal_places=2)
    imagen = models.ImageField(upload_to="home/static")
    encuesta= models.ForeignKey(Encuesta, on_delete=models.CASCADE, editable=False)

    def save(self):
            self.encuesta = Encuesta.objects.latest('date')
            super(Marca, self).save()

    def __str__(self):
        return self.nombre

class Opciones(models.Model):
    nIteracion=models.IntegerField()
    encuesta= models.ForeignKey(Encuesta, on_delete=models.CASCADE, editable=False)
    #encuesta= models.IntegerField()
    marca= models.ForeignKey(Marca, on_delete=models.CASCADE, editable=False)

    def __str__(self):
        return self.nIteracion
