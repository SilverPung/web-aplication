
# Create your views here.
from django.shortcuts import render,get_object_or_404,redirect
from .models import Item,Category
from django.contrib.auth.decorators import login_required
from .forms import NewItemForm,EditItemForm



def detail(request,pk):#funkcja odpowiadająca za wyświetlanie strony z danymi przedmiotu
    item=get_object_or_404(Item,pk=pk)#pobranie przedmiotu z bazy danych
    related_items=Item.objects.filter(category=item.category, is_sold=False).exclude(pk=item.pk)#pobranie przedmiotów z tej samej kategorii
    return render(request, 'item/detail.html', {'item': item, 'related_items': related_items})#wyświetlenie strony z danymi przedmiotu

def category(request,pk):#funkcja odpowiadająca za wyświetlanie strony z przedmiotami z danej kategorii
    category=get_object_or_404(Category,pk=pk)#pobranie kategorii z bazy danych
    items=Item.objects.filter(category=category, is_sold=False)#pobranie przedmiotów z danej kategorii
    related_categories=Category.objects.exclude(pk=category.pk)#pobranie kategorii z wyłączeniem kategorii z której pobierane są przedmioty
    return render(request, 'item/category.html', {'items': items, 'category': category,'related_categories':related_categories})#wyświetlenie strony z przedmiotami z danej kategorii


@login_required
def new(request):  #funkcja odpowiadająca za wyświetlanie strony z formularzem dodawania nowego przedmiotu
    if request.method == 'POST':   
        form = NewItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
            return redirect('item:detail', pk=item.id)
    else:
        form=NewItemForm()
    return render(request, 'item/new.html', {'form':form})   #wyświetlenie strony z formularzem dodawania nowego przedmiotu  

@login_required
def delete(request,pk):
    item = get_object_or_404(Item, pk=pk,created_by=request.user)
    item.delete()
    return redirect('dashboard:index')

@login_required
def edit(request,pk):  #funkcja odpowiadająca za wyświetlanie strony z formularzem dodawania nowego przedmiotu
    item = get_object_or_404(Item, pk=pk,created_by=request.user)
    if request.method == 'POST':   
        form = EditItemForm(request.POST, request.FILES,instance=item)
        if form.is_valid():
            form.save()
            return redirect('item:detail', pk=item.id)
    else:
        form=EditItemForm(instance=item)
    return render(request, 'item/edit.html', {'form':form})   #wyświetlenie strony z formularzem dodawania nowego przedmiotu  


