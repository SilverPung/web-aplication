from django.urls import path
from . import views

app_name = 'core' #nazwa podaplikacji

urlpatterns = [ #adresy url na stronie odpowiadające za wywołanie funkcji z pliku views.py
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.signup, name='signup')
]