from django.urls import path
from . import views

#plik odpowiadający za adresy url na stronie które wywołują funkcje z pliku views.py

app_name = 'item'#nazwa podaplikacji
urlpatterns = [#adresy url na stronie odpowiadające za wywołanie funkcji z pliku views.py
    path('<int:pk>/', views.detail, name='detail'),
]