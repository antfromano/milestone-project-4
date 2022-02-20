from django.db import models
from django.db.models.functions import Coalesce
from django.db.models import IntegerField, Model
from django.core.validators import MaxValueValidator, MinValueValidator

class Content(models.Model):

    class Meta:
        verbose_name_plural = 'Contents'

    name = models.CharField(max_length=254)
    
    def __str__(self):
        return self.name

class Work(models.Model):

    class Meta:
        verbose_name_plural = 'Works'

    content = models.ForeignKey('Content', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    description = models.TextField()
    is_sold = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)

    def avg_rating(self):
        return Rating.objects.filter(movie=self).aggregate(
                avg=Coalesce(models.Avg('number'), 0),
            )['avg']

    def __str__(self):
        return self.name
