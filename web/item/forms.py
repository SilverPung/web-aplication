from django import forms
from .models import Item

TEXT_INPUT = 'w-full py-4 px-6 rounded-xl border'
class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'category','description', 'price', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name', 'class': TEXT_INPUT}),
            'category': forms.Select(attrs={'placeholder': 'Category', 'class': TEXT_INPUT}),
            'description': forms.Textarea(attrs={'placeholder': 'Description', 'class': TEXT_INPUT}),
            'price': forms.NumberInput(attrs={'placeholder': 'Price', 'class': TEXT_INPUT}),
            'image': forms.FileInput(attrs={'placeholder': 'Image', 'class': TEXT_INPUT}),
        }

class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'category','description', 'price', 'image','is_sold']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name', 'class': TEXT_INPUT}),
            'category': forms.Select(attrs={'placeholder': 'Category', 'class': TEXT_INPUT}),
            'description': forms.Textarea(attrs={'placeholder': 'Description', 'class': TEXT_INPUT}),
            'price': forms.NumberInput(attrs={'placeholder': 'Price', 'class': TEXT_INPUT}),
            'image': forms.FileInput(attrs={'placeholder': 'Image', 'class': TEXT_INPUT}),
            'is_sold': forms.CheckboxInput(attrs={'placeholder': 'Is sold', 'class': TEXT_INPUT + 'text-left'}),
        }