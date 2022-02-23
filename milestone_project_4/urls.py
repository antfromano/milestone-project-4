"""milestone_project_4 URL configuration
the `urlpatterns` list routes URLs to views. for more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
examples:
function views
    1. add an import:  from my_app import views
    2. add a URL to urlpatterns:  path('', views.home, name='home')
class-based views
    1. add an import:  from other_app.views import home
    2. add a URL to urlpatterns:  path('', Home.as_view(), name='home')
including another URLconf
    1. import the include() function: from django.urls import include, path
    2. add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('works/', include('works.urls')),
    path('cart/', include('cart.urls')),
    path('checkout/', include('checkout.urls')),
    path('profile/', include('profiles.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
