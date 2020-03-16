from django.shortcuts import render, redirect
from product.models import ItemModel
from product.forms import CreateItemForm
from accounts.models import Account
from shops.models import ShopsData


def product_view(request):
    context = {}
    user = request.user
    items = ItemModel.objects.filter(item_from_shop__shop_owner=user.id).all()
    context['shop_item'] = items
    return render(request, 'product/view_product.html', context)


def create_product_view(request):
    context = {}
    user = request.user
    if not user.is_authenticated:
        return redirect('accounts:m_auth')
    form = CreateItemForm(request.POST or None, request.FILES or None)
    custom_user = Account.objects.get(id=user.id)
    if form.is_valid():
        obj = form.save(commit=False)
        shop_data = ShopsData.objects.filter(shop_owner=user.id).first()
        custom_user.is_shop_owner = True
        custom_user.save()
        obj.item_from_shop = shop_data
        obj.save()
        form = CreateItemForm(
            initial=None
        )
        return redirect('products:create_product_for_shop')
    context['product_form'] = form
    context['custom_user'] = custom_user
    return render(request, 'product/create_product_form.html', context)
