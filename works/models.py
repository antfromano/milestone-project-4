from django.db import models

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
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True,
                                 blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
