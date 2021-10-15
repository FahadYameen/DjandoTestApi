from django.db import models

# Create your models here.

class Post(models.Model):
    auto_increment_id = models.AutoField(primary_key=True)
    score = models.FloatField(default=None)
    title = models.TextField(default=None)