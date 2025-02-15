from django import forms
from .models import Order, Item




STATUS_CHOICES = [
    ('pending', 'Pending'),
    ('ready', 'Ready'),
    ('paid', 'Paid'),
]
TABLE_CHOICES = [
    ("1", "Стол 1"),
    ("2", "Стол 2"),
    ("3", "Стол 3"),
    ("4", "Стол 4"),
    ("5", "Стол 5"),
    ("6", "Стол 6"),
    ("7", "Стол 7"),
    ("8", "Стол 8"),
    ("9", "Стол 9"),
    ("10", "Стол 10"),
]
class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ['table_number', 'items', 'status']
        widgets = {
            'status': forms.Select(choices=STATUS_CHOICES),
            'table_number': forms.Select(choices=TABLE_CHOICES),
        }

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['items'].queryset = Item.objects.all()



class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'price', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }