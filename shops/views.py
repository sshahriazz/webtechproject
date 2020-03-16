from django.shortcuts import render, redirect
from shops.forms import CreateShopForm
from accounts.models import Account
from shops.models import ShopsData


def create_shop_view(request):
    context = {}
    user = request.user
    if not user.is_authenticated:
        return redirect('accounts:m_auth')
    form = CreateShopForm(request.POST or None, request.FILES or None)
    custom_user = Account.objects.get(id=user.id)
    if form.is_valid():
        obj = form.save(commit=False)
        shop_owner = Account.objects.filter(email=user.email).first()
        custom_user.is_shop_owner = True
        custom_user.save()
        obj.shop_owner = shop_owner
        obj.save()
        form = CreateShopForm(
            initial=None
        )
        return redirect('shops:shop_view')
    context['shop_form'] = form
    context['custom_user'] = custom_user
    return render(request, 'shops/create_shop_form.html', context)


def shop_view(request):
    context = {}
    user = request.user
    if not user.is_authenticated:
        return redirect('accounts:m_auth')
    shop_owner = Account.objects.filter(email=user.email).first()
    shop = ShopsData.objects.filter(shop_owner=shop_owner).first()
    context['shop_data'] = shop
    return render(request, 'shops/shop_view.html', context)