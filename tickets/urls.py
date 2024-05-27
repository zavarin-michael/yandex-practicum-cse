from django.urls import path

from tickets import views

urlpatterns = [
    path('', views.get_tickets_page, name='tickets'),
]
