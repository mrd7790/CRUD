from django.urls import path, include


urlpatterns = [
    path('api/sp/', include('api.urls')),
]
