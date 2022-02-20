from django.contrib import admin
from .models import Work, Content, Review

class WorkAdmin(admin.ModelAdmin):
    list_display = (
        'content',
        'name',
        'price',
        'rating',
        'is_sold',
        'image',
    )

    ordering = ('content',)

admin.site.register(Work, WorkAdmin)
admin.site.register(Content)
admin.site.register(Review)
