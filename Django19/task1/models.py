from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()

    def __str__(self):
        return self.title

class Buyer(models.Model):
    name = models.CharField(max_length=30)
    balance = models.DecimalField(decimal_places=2, max_digits=6)
    age = models.IntegerField()

    def __str__(self):
        return self.name

class Game(models.Model):
    title = models.CharField(max_length=30)
    cost = models.DecimalField(decimal_places=2, max_digits=6)
    size = models.DecimalField(decimal_places=2, max_digits=6)
    description = models.TextField()
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer, related_name='buyers')

    def __str__(self):
        return self.title

'''
QUERYSET

python manage.py shell
>>> from task1.models import Post
>>> Post.objects.create(title='title1', description='desc1')
>>> Post.objects.create(title='title2', description='desc2')
>>> Post.objects.create(title='title2', description='desc2')

>>> post = Post.objects.get(id=1)
>>> post.title = 'New title'
>>> post.save
>>> post.save()

>>> Post.objects.all()
>>> post = Post.objects.get(id=3)
>>> post.delete()

>>> Post.objects.filter(title='title2')  
'''