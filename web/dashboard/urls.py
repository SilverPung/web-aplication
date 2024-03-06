from django.urls import path
from . import views
app_name = 'dashboard' #nazwa podaplikacji

urlpatterns = [ #adresy url na stronie odpowiadające za wywołanie funkcji z pliku views.py
    path('', views.index, name='index'),
    
]