from django.shortcuts import render
from accounts.models import Account


def index(request):
    context = {}
    if request.user.is_authenticated:
        accounts = Account.objects.all()
        context['accounts'] = accounts
        return render(request, 'baseapp/index.html', context)
    else:
        return render(request, 'baseapp/index.html', context)
