from django.urls import path

from . import views

item_url_patterns = [
    path('', views.ApiOverview, ),
    path('item/create', views.add_item, name='add_item'),
    path('item/update/<int:pk>', views.update_item, name='update_item'),
    path('item/delete/<str:pk>', views.delete_item, name='delete-items'),
    path('item/getAll', views.view_items, name='view_items'),
    path('item/test', views.test, name='test'),
]

__exports__ = item_url_patterns
