"""
URL configuration for web project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static  #nie robić tego w produkcji

from django.contrib import admin
from django.urls import path, include
from core.views import index,contact

urlpatterns = [
    path('', include('core.urls')),#podaplikacja core gdzie odsyłamy do pliku urls.py z core
    path('items/', include('item.urls')), #podaplikacja items gdzie odsyłamy do pliku urls.py z item
    path('dashboard/', include('dashboard.urls')), #podaplikacja dashboard gdzie odsyłamy do pliku urls.py z dashboard
    path('inbox/', include('conversation.urls')), #podaplikacja conversation gdzie odsyłamy do pliku urls.py z conversation
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #nie robić tego w produkcji
