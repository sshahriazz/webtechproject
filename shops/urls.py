from django.urls import path, include
from shops.views import create_shop_view, shop_view
app_name = 'shops'
urlpatterns = [
    path('', shop_view, name='shop_view'),
    path('create/', create_shop_view, name='create_shop'),
]
