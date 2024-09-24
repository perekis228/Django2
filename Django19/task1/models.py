from django.db import models

# Create your models here.
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
>>> from task1.models import Buyer
>>> Buyer.objects.create(name='Garry', balance=111.11, age=12)
>>> Buyer.objects.create(name='Alex', balance=5690.1, age=19)
>>> Buyer.objects.create(name='Tonny', balance=3010.9, age=33)

>>> from task1.models import Game
>>> Game.objects.create(title='GTA5', cost=3000, size=112, description='rob and kill', age_limited=True)
>>> Game.objects.create(title='PayDay2', cost=1500, size=44, description='rob and rob', age_limited=True)
>>> Game.objects.create(title='Kindergarten', cost=100, size=19, description='peace bro', age_limited=False)

>>> garry = Buyer.objects.get(id=1)
>>> alex = Buyer.objects.get(id=2) 
>>> tonny = Buyer.objects.get(id=3) 

>>> Game.objects.get(id=1).buyer.set((alex, tonny))               
>>> Game.objects.get(id=2).buyer.set((alex, tonny))               
>>> Game.objects.get(id=3).buyer.set((alex, garry))
'''