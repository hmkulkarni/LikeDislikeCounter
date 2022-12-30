from django.db import models

class Like(models.Model):
    countLikes = models.IntegerField(default=0)

class Dislike(models.Model):
    countDislikes = models.IntegerField(default=0)