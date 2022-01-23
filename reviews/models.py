from django.db import models
from works.models import Work, Content
from django.core.validators import MaxValueValidator, MinValueValidator


class Rating(models.Model):

    class Meta:
        verbose_name_plural = 'Rating'

    name = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True, default=1, validators=[
                                 MaxValueValidator(5), MinValueValidator(1)])

    def __str__(self):
        return self.name

class Review(models.Model):

    class Meta:
        verbose_name_plural = 'Reviews'

    rating = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True, default=1, validators=[
                                 MaxValueValidator(5), MinValueValidator(1)])

    def __str__(self):
        return self.name
