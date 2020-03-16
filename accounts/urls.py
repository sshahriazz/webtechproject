from django.urls import path
from accounts.views import registration_view, logout_view, login_view, account_view, must_authenticate_view
from django.contrib.auth import views as auth_views

app_name = "accounts"
urlpatterns = [
    path('', account_view, name='profile'),
    path('register/', registration_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('login/', login_view, name='login'),
    path('must_authenticate', must_authenticate_view, name='m_auth')
]
