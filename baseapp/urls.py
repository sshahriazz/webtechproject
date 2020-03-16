from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from baseapp.views import index

urlpatterns = [
    path('', index, name="home"),
    path('admin/', admin.site.urls),
    path('accounts/', include("accounts.urls", namespace="accounts")),
    path('shop/', include('shops.urls', namespace="shops")),
    path('product/', include('product.urls', namespace="products"))

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
