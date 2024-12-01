from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('api/data/', include("api_data.urls")),
     path('api/model/', include("api_model.urls")),
    path('admin/', admin.site.urls)
]
