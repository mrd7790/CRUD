from django.urls import path

from . import views
from . import mixin

item_url_patterns = [
    path('', views.api_over_view, ),
    path('item', views.add_item, name='add_item'),
    path('item/<str:pk>', views.item_manipulate, name='item_get_update_delete'),
    path('item/get-all/', views.get_all_items, name='get_all_items'),

    # mixin url
    path('mixin', mixin.item_detail),
    path('mixin/<str:pk>', mixin.item_detail),
]

__exports__ = item_url_patterns
