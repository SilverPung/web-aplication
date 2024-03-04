from django.db import models
from django.contrib.auth.models import User


#modele odpowiadające tabelom w bazie danych

class Category(models.Model):#model kategorii
    name = models.CharField(max_length=255)

    class Meta:#klasa odpowiadająca za wyświetlanie kategorii w panelu admina
        ordering = ('name',)
        verbose_name_plural = 'categories'

    def __str__(self):#funkcja odpowiadająca za wyświetlanie nazwy kategorii
        return self.name
    
class Item(models.Model):#model przedmiotu
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category,related_name='items',on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='item_images',blank=True, null=True)
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User,related_name='items',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:#klasa odpowiadająca za wyświetlanie przedmiotów w panelu admina
        ordering = ('name',)

    def __str__(self):#funkcja odpowiadająca za wyświetlanie nazwy przedmiotu
        return self.name
