from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from shop import views


urlpatterns = [
    path('pvb-admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('offer/', include('offers.urls')),
    path('shop/', include('shop.urls')),
    path('cart/', include('cart.urls')),
] 

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
