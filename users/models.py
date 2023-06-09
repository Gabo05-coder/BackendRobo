from django.db import models

# Create your models here.
class Users(models.Model):
    username = models.CharField(max_length=60)
    email = models.EmailField()
    password = models.CharField(max_length=12)
    profilePicture = models.ImageField(blank=True, upload_to='media/profile_pics/')

    def __str__(self):
        return self.username