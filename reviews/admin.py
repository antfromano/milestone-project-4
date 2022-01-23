from django.contrib import admin
from .models import Rating, Review

class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'rating',
    )

admin.site.register(Review, ReviewAdmin)
admin.site.register(Rating)
