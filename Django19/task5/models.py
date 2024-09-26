from django.db import models

# Create your models here.
class Comix(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    year = models.IntegerField()

    def __str__(self):
        return self.title