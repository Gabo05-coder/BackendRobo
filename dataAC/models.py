from django.db import models

# Create your models here.
#clase de aire acondicionado (entidad a lo que entendi)   
class dataAC(models.Model):
    name=models.CharField(max_length=6)
    mark=models.CharField(max_length=20)
    model=models.CharField(max_length=30)
    location=models.CharField(max_length=20)
    conectionCode=models.CharField(max_length=10)