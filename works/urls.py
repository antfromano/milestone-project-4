from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_works, name='works'),
    path('<work_id>', views.work_item, name='work_item'),
]
