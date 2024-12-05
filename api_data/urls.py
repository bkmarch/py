from django.urls import path

from . import views

urlpatterns = [
    path('all/', views.getAllData),
    path('add/', views.addItem),
    path('company/<int:company_id>/', views.getCompany),
    path('equityaward/<int:award_id>/', views.getEquityAwardData),
    path('executive/<int:executive_id>/', views.getExecutive),
    path('company/<int:company_id>/equityawards/', views.getCompanyEquityAwards)
]