from django.urls import path, include

from . import views

urlpatterns = [
    path('users/', include('apps.accounts.urls'), name="User handler"),
    path('course/', include('apps.courses.urls'))
]