from django.db import models
from users.models import Users

# Create your models here.
class Posts(models.Model):
    author = models.ForeignKey(Users, on_delete=models.CASCADE, blank=False)
    description = models.TextField()
    postPicture = models.ImageField(blank=True)
    createdDate = models.DateField(auto_now_add=True)
    date = models.DateField(blank=False)

    def __str__(self):
        return self.description

class Likes(models.Model):
    likedPost = models.ManyToManyField(Posts, blank=False)
    likerUser = models.ManyToManyField(Users, blank=False)

    def __str__(self):
        return self.likedPost, self.likerUser

class Participants(models.Model):
    participatedPost = models.ManyToManyField(Posts, blank=False)
    participatingUsers = models.ManyToManyField(Users, blank=False)

    def __str__(self):
        return self.participatedPost, self.participatingUsers