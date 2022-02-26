from django.urls import path

from . import views

urlpatterns = [
    path('', views.ApiOverview, ),
    path('create/', views.add_item, name='add_item'),
    path('createall/', views.add_items, name='add_items'),
    path('all/', views.view_items, name='view_items'),
    path('update/<int:pk>', views.update_item, name='update_item'),
    path('item/<int:pk>/delete/', views.delete_item, name='delete-items'),
]
