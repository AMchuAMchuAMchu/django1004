from django.http import HttpResponse

# Create your views here.
from django.shortcuts import render

from myapp import models

user_list = [
    {'username':'雪之下雪乃','password':'5201314'},
    {'username':'堀北铃音','password':'520'},
    {'username':'楪祈','password':'52013141314'},
]

def index(request):
    global user_list
    if request.method == 'POST':
        if request.POST.get('username') != '' and request.POST.get('password') != '':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = {'username':username,'password':password}
            user_list.append(user)
            models.UserInfo.objects.create(username=username,password=password)
            userInfoQuerySet = models.UserInfo.objects.all()
            user_list = list(userInfoQuerySet)
    return render(request,'index.html',{'data':user_list})