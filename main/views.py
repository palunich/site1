from django.http import HttpResponse
from django.shortcuts import render
from .models import User


def index(request):

    user=User.objects.filter(email=request.GET['email'],passw=request.GET['passw'])
    if len(user) > 0:
        money=user[0].money
        user[0].money=money-1
        #доавить в список фотона с каким NetId не удалять из игры -
        # в цикле удаления убирать защиту каждый раз при неудалении
        user[0].save()
        return HttpResponse(user[0].money)
    else:
        return HttpResponse("0")


def login(request):
    if request.POST['email']=='admin' and request.POST['passw']=='admin':
        return HttpResponse("ok")
    else:
        return HttpResponse("bad")


def form(request):
    return render(request, 'form.html')
