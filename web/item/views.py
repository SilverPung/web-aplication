from django.shortcuts import render,get_object_or_404
from .models import Item
# Create your views here.
def detail(request,pk):#funkcja odpowiadająca za wyświetlanie strony z danymi przedmiotu
    item=get_object_or_404(Item,pk=pk)#pobranie przedmiotu z bazy danych
    related_items=Item.objects.filter(category=item.category, is_sold=False).exclude(pk=item.pk)#pobranie przedmiotów z tej samej kategorii
    return render(request, 'item/detail.html', {'item': item, 'related_items': related_items})#wyświetlenie strony z danymi przedmiotu