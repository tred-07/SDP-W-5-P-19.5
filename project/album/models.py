from django.db import models
from musician.models import Musician 
# Create your models here.

class Album(models.Model):
    name=models.CharField(max_length=40)
    musician=models.ForeignKey(Musician,on_delete=models.CASCADE)
    releaseDate=models.DateField()
    rating=models.IntegerField(choices=[(1, 1),(2,2),(3,3),(4,4),(5,5)])

    def __str__(self):
        return f'Name: {self.name}, Musician: {self.musician}'