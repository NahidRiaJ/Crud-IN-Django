from django.contrib import admin
from django.urls import path, include
from .SimpleView import simple_view   # correctly importing the view

urlpatterns = [
    # path('admin/', admin.site.urls),  # Enable admin panel
    path('myapp/', include('myapp.urls')),
    path('Product/', include('Product.urls')),
    path('categories/', include('Categories.urls')),
    path('accounts/', include('accounts.urls')),
    path('', simple_view),  # Home page
]
