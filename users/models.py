from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
# Create your models here.

UserModel = get_user_model()

class Note(models.Model):
    noteTitle = models.TextField()
    noteText = models.TextField()
    pubDate = models.DateTimeField("date published")
    colorR = models.IntegerField()
    colorG = models.IntegerField()
    colorB = models.IntegerField()
    category = models.TextField()
    creator = models.ForeignKey(UserModel, on_delete=models.SET_NULL, null=True)
    #Foreign key = user
    
    def __str__(self):
        return self.noteText
        
