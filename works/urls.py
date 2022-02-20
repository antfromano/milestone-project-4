from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_works, name='works'),
    path('<int:work_id>/', views.work_item, name='work_item'),
    path('add/', views.add_work, name='add_work'),
    path('edit/<int:work_id>/', views.edit_work, name='edit_work'),
    path('delete/<int:work_id>/', views.delete_work, name='delete_work'),
    path('review/<int:work_id>/', views.review_work, name='review_work'),    
    ]
