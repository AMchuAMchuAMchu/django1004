from django.http import HttpResponse

# Create your views here.
from django.shortcuts import render, redirect

from myapp import models

user_list = [
    # {'username':'雪之下雪乃','password':'5201314'},
    # {'username':'堀北铃音','password':'520'},
    # {'username':'楪祈','password':'52013141314'},
]


# 通过cookie判断当前进入该网页的用户是否有权限访问该页面...
def session_judge(request):
    username01 = request.session.get('username')
    password01 = request.session.get('password')
    print('username01>',username01)
    print('password01>',password01)
    person01 = models.UserInfo.objects.filter(username=username01, password=password01)
    print('>>>>',person01)
    count = person01.count()
    return count


def index(request):
    global user_list
    count = session_judge(request)
    print('>>>',count)
    if count > 0:
        if request.method == 'POST':
            # 健壮性判断
            if request.POST.get('username') != '' and request.POST.get('password') != '':
                username = request.POST.get('username')
                password = request.POST.get('password')
                user = {'username': username, 'password': password}
                user_list.append(user)
                models.UserInfo.objects.create(username=username, password=password)
                userInfoQuerySet = models.UserInfo.objects.all()
                user_list = list(userInfoQuerySet)
        # 就是的话是在你初次渲染的时候记得还是需要直接从数据库中获取数据的说....
        userInfoQuerySet = models.UserInfo.objects.all()
        print('>>>>>>>',userInfoQuerySet)
        user_list = list(userInfoQuerySet)
        return render(request, 'index.html', {'data': user_list})
    else:
        return render(request, 'u_error.html')


def login(request):
    return render(request, 'login.html')


def handle_login(request):
    count = session_judge(request)
    if count > 0:
        return redirect(to='/index/',request=request)
    username = request.POST.get('username')
    password = request.POST.get('password')
    record = models.UserInfo.objects.filter(username=username, password=password)
    if record.count() > 0:
        request.session['username']=username
        request.session['password']=password
        request.session.set_expiry(value=60)
        return redirect(to='/index/',request=request)
    return render(request,'u_error.html')
