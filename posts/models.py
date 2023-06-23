from django.db import models
from users.models import Users

# Create your models here.
class Posts(models.Model):
    author = models.ForeignKey(Users, on_delete=models.CASCADE, blank=False)
    description = models.TextField()
    postPicture = models.ImageField(blank=False, upload_to='posts/')
    createdDate = models.DateField(auto_now_add=True)
    date = models.DateField(blank=False, null=True)
    likes = models.ManyToManyField(Users, related_name='likers', blank=True)
    participants = models.ManyToManyField(Users, related_name='participants', blank=True)

    def __str__(self):
        return self.description