from django.db import models
from django.db.models import CharField


class Post(models.Model):
    text = models.TextField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.text

