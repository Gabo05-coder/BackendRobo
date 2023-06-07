from django.contrib import admin
from .models import Likes, Participants, Posts

# Register your models here.
admin.site.register(Likes)
admin.site.register(Participants)
admin.site.register(Posts)