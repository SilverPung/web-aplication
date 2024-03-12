from django.urls import path
from . import views

#plik odpowiadający za adresy url na stronie które wywołują funkcje z pliku views.py

app_name = 'conversation'  #nazwa podaplikacji
urlpatterns = [    #adresy url na stronie odpowiadające za wywołanie funkcji z pliku views.py
    path('new/<int:item_pk>/', views.new_conversations, name='new'),
    path('inbox/', views.inbox, name='inbox'),
    path('detail/<int:conversation_pk>/', views.detail, name='detail'),
]