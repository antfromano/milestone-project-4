from django.urls import path
from . import views

urlpatterns = [
    path('review_work/<int:work_id>/', views.review_work, name='review_work'),
]