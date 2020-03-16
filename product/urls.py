from django.urls import path
from product.views import product_view, create_product_view

app_name = 'products'

urlpatterns = [
    path('', product_view, name='product_view_for_shop'),
    path('create_product/', create_product_view, name='create_product_for_shop')
]
