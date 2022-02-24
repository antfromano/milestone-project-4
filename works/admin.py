from django.contrib import admin
from .models import Work, Content, Review


class WorkAdmin(admin.ModelAdmin):
    list_display = (
        'content',
        'name',
        'price',
        'is_sold',
        'image',
    )

    ordering = ('content',)

"""
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'work',
        'user_rating',
        'comment',
        'user',
        'created_on',
    )

    ordering = ('work',)
"""

class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'work',
        'user_rating',
        'comment',
        'user',
        'created_on',
    )
    list_filter = ('active', 'created_on')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)

admin.site.register(Work, WorkAdmin)
admin.site.register(Content)
admin.site.register(Review, ReviewAdmin)
