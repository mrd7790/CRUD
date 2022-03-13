from django.urls import path

from . import views

item_url_patterns = [
    path('', views.api_over_view, ),
    path('item/', views.add_item, name='add_item'),
    path('item/<str:pk>/', views.get_item, name='get_item'),
    path('item/get-all/', views.get_all_items, name='get_all_items'),
    path('item/<str:pk>/', views.update_item, name='update_item'),
    path('item/<str:pk>/', views.patch_item, name='patch_item'),
    path('item/<str:pk>/', views.delete_item, name='delete-item'),
    path('item/test', views.test, name='test'),
]

__exports__ = item_url_patterns
