from django.http import HttpResponse

# Create your views here.
from django.shortcuts import render


user_list = [
    {'username':'雪之下雪乃','password':'5201314'},
    {'username':'堀北铃音','password':'520'},
    {'username':'楪祈','password':'52013141314'},
]

def index(request):
    if request.method == 'POST':
        if request.POST.get('username') is not '' and request.POST.get('password') is not '':
            user = {'username':request.POST.get('username'),'password':request.POST.get('password')}
            user_list.append(user)
    return render(request,'index.html',{'data':user_list})