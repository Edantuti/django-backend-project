from django.urls import path

from . import views

urlpatterns = [
    path('', views.CourseData.as_view()),
    path('details/<str:pk>', views.CourseDetail.as_view()),
    path('enroll/', views.EnrollData.as_view()),
    path('video/', views.VideoData.as_view()),
    path('video/<str:pk>', views.VideoDetail.as_view())
]
