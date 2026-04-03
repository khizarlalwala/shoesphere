from django.db import models

# Create your models here.
from django.db import models

class Shoe(models.Model):

    name=models.CharField(max_length=200)

    price=models.IntegerField()

    image=models.URLField()

    def __str__(self):
        return self.name