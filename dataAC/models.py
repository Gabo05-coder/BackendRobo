from django.db import models

# Create your models here.


#clase de aire acondicionado (entidad a lo que entendi)   
class dataAC(models.Model):

    MODE_CHOICES = (
        ('Auto', 'Auto'),
        ('Manual', 'Manual'),
    )

    STATUS_CHOICES = (
        ('On', 'On'),
        ('Off', 'Off'),
    )

    name=models.CharField(max_length=6)
    mark=models.CharField(max_length=20)
    model=models.CharField(max_length=30)
    location=models.CharField(max_length=20)
    conectionCode=models.CharField(max_length=10)
    mode = models.CharField(max_length=10, choices=MODE_CHOICES, default='Auto')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Off')

    ## Campos para modo y estado EXPERIMENTAL pa horny






#def __str__(self):
#   return f'AC - Mode: {self.mode}, STATUS: {self.status}'