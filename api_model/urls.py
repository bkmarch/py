from django.urls import path


from . import views

urlpatterns = [
    path("equityawardvalue/<int:award_id>/", views.EquityAwardValue, name = "EquityAwardValue")
]