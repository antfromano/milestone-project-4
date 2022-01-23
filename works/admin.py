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

class ReviewAdmin(admin.ModelAdmin):
    readonly_fields = (
        'content',
        'name',
        'price',
        'is_sold',
        'image',
    )
    list_display = (
        'rating',
    )

admin.site.register(Work, WorkAdmin)
admin.site.register(Content)
