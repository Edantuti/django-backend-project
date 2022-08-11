from django.urls import path, include

from . import views

urlpatterns = [
    path('users/', include('apps.accounts.urls'), name="User handler"),
    path('course/', views.getCourse),
    path('course/create/', views.createCourse),
    path('course/delete/', views.deleteCourse),
    path('course/update/', views.updateCourse)
]
