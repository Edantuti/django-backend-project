from django.http import HttpResponse, Http404
# from apps.accounts.models import User
from django.contrib.auth.models import User


# Create your views here.




def deleteUser(request):
    return HttpResponse("Delete user")

def createCourse(request):
    return HttpResponse("Created Course")

def updateCourse(request):
    return HttpResponse("Updated")

def getCourse(request):
    return HttpResponse("Get")

def deleteCourse(request):
    return HttpResponse("Deleted")


