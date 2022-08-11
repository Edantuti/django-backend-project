from django.urls import path

from . import views

urlpatterns = [
    path('', views.CourseData.as_view()),
    path('<str:pk>', views.CourseDetail.as_view()),
    path('enroll/', views.EnrollData.as_view())
]
