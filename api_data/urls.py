from django.urls import path


from . import views

urlpatterns = [
    path('getall/', views.getAllData),
    path('add/', views.addItem),
    path('getequityaward/', views.getEquityAwardData)
]