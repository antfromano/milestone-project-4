from django.contrib import admin
from .models import Work, Content

# Register your models here.

class WorkAdmin(admin.ModelAdmin):
    list_display = (
        'content',
        'name',
        'price',
        'rating',
        'image',
    )

    ordering = ('content',)

admin.site.register(Work, WorkAdmin)
admin.site.register(Content)
