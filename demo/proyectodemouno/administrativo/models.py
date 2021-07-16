from django.db import models

# Create your models here.
class Provincia(models.Model):
    nombre = models.CharField(max_length=30)
    capital_provincial = models.CharField(max_length=30)
    poblacion = models.IntegerField("Poblacion de la provincia")

    def __str__(self):
        return "%s - %s - %s - edad: %d" % (self.nombre, 
                self.nombre,
                self.capital_provincial,
                self.poblacion)
