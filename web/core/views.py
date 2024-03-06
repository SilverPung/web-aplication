from django.shortcuts import render, redirect
from item.models import Category, Item
from .forms import SignupForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
# Create your views here.
# funkcje odpowiadające za wyświetlanie stron wywyują się po wpisaniu odpowiedniego adresu url z pliku urls.py
def index(request):#funkcja odpowiadająca za wyświetlanie strony głównej
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()
    return render(request, 'core/index.html', {'items': items, 'categories': categories})

def contact(request):#funkcja odpowiadająca za wyświetlanie strony kontaktowej
    return render(request, 'core/contact.html')

def signup(request):#funkcja odpowiadająca za wyświetlanie strony rejestracji
    if request.method == 'POST':#jeżeli metoda jest POST to wywołaj formularz
        form = SignupForm(request.POST)#formularz
        if form.is_valid():
            form.save()
        return redirect('/login/')#przekierowanie na stronę logowania
    else:
        form = SignupForm()
    return render(request, 'core/signup.html', {'form': form})#wyświetlenie strony rejestracji


def logout_view(request):#funkcja odpowiadająca za wylogowanie
    if request.method == 'POST':
        logout(request)
        return redirect('/')
    return render(request, 'core/logout.html')#wyświetlenie strony wylogowania

