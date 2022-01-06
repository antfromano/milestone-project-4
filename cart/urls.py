from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_cart, name='view_cart'),
    path('add/<work_id>/', views.add_to_cart,
         name='add_to_cart'),
    path('adjust/<work_id>/', views.adjust_cart,
         name='adjust_cart'),
    path('remove/<work_id>/', views.remove_from_cart,
         name='remove_from_cart'),
]
