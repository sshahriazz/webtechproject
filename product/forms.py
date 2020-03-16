from django import forms
from product.models import ItemModel


class CreateItemForm(forms.ModelForm):
    class Meta:
        model = ItemModel
        fields = [
            'item_name',
            'item_description',
            'item_regular_price',
            'item_discounted_price',
            'item_quantity',
            'item_image1',
            'item_image2',
            'item_image3'
        ]