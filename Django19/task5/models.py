from django.db import models

# Create your models here.
class Comix(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    year = models.IntegerField()

    def __str__(self):
        return self.title

class Test(models.Model):
    id = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=10)

    def __str__(self):
        return self.Name

'''
>>> from task5.models import Test
>>> Test.objects.all()           
<QuerySet [<Test: AAAA>, <Test: BBBB>]>
>>> Test.objects.get(id=2)
<Test: BBBB>
>>> Test.objects.create(id=3, Name='AAAA') 
<Test: AAAA>
>>> Test.objects.filter(Name='AAAA')
<QuerySet [<Test: AAAA>, <Test: AAAA>]>
>>> len(Test.objects.all())
3
'''