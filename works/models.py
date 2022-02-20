from django.db import models
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
    rating = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True, default=1, validators=[
                                 MaxValueValidator(5), MinValueValidator(1)])
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

class Review(models.Model):

    class Meta:
        verbose_name_plural = 'Reviews'

    work = models.ForeignKey('Work', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    user_rating = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True, default=1, validators=[
                                 MaxValueValidator(5), MinValueValidator(1)])
    comment = models.CharField(max_length=200, default='')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.review
