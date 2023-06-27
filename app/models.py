from django.db import models

class Pan(models.Model):

    codigo              = models.IntegerField()
    nombre              = models.CharField(max_length=20)
    precio              = models.IntegerField()
    descripcion         = models.TextField()
    imagen              = models.ImageField(upload_to="productos", null=True)  

    def __str__(self):
        return self.nombre 


