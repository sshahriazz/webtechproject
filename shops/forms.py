from django import forms
from shops.models import ShopsData


class CreateShopForm(forms.ModelForm):
    class Meta:
        model = ShopsData
        fields = ['shop_name', 'shop_description', 'shop_front_image']
