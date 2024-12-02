from django.urls import path


from . import views

urlpatterns = [
    path('getall/', views.getAllData),
    path('add/', views.addItem),
    path('getequityaward/<int:award_id>/', views.getEquityAwardData),
    path('getexecutive/<int:executive_id>/', views.getExecutive)
]