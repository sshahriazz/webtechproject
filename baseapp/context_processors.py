from django.shortcuts import redirect
from accounts.models import Account


def add_variable_to_template(request):
    user = request.user
    if not user.is_authenticated:
        return {
            'title': 'App Name',
        }
    else:
        custom_user = Account.objects.get(id=user.id)
        return {
            'title': 'App Name',
            'custom_user': custom_user
        }