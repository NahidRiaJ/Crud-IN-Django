from django.urls import path
from . import views

urlpatterns = [
    path('', views.item_list, name='item_list'),
    path('item/<int:id>/', views.item_detail, name='item_detail'),  # fixed name
    path('create/', views.create_item, name='create_item'),         # fixed name
    path('update/<int:id>/', views.update_item, name='update_item'),
    path('delete/<int:id>/', views.delete_item, name='delete_item'),
]
