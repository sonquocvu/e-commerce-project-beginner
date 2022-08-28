from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shopping/', include('djoser.urls')),
    path('shopping/', include('djoser.urls.authtoken')),
    path('shopping/', include('product.urls'))
]
