
# Create your views here.
from django.shortcuts import render,get_object_or_404
from .models import Item
from django.contrib.auth.decorators import login_required
from .forms import NewItemForm



def detail(request,pk):#funkcja odpowiadająca za wyświetlanie strony z danymi przedmiotu
    item=get_object_or_404(Item,pk=pk)#pobranie przedmiotu z bazy danych
    related_items=Item.objects.filter(category=item.category, is_sold=False).exclude(pk=item.pk)#pobranie przedmiotów z tej samej kategorii
    return render(request, 'item/detail.html', {'item': item, 'related_items': related_items})#wyświetlenie strony z danymi przedmiotu


@login_required
def new(request):  #funkcja odpowiadająca za wyświetlanie strony z formularzem dodawania nowego przedmiotu
    item_form=NewItemForm(request.POST, request.FILES)
    return render(request, 'item/new.html', {'form':item_form})   #wyświetlenie strony z formularzem dodawania nowego przedmiotu  

