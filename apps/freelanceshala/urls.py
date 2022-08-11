from django.urls import path

from . import views

urlpatterns=[
    path('', views.OrdersData.as_view())
]