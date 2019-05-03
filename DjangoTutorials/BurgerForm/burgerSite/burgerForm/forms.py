from django import forms

from .models import Order

class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ('order_number', 'customer_name', 'protein', 'num_patties', 'cook', 'lettice', 'tomato', 'onion', 'cheese', 'bun', 'sauce', 'comments', 'date');
