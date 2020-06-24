from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.shortcuts import redirect
from . import models


# Create your views here.


def index(request):
    pass
    return render(request, 'login/index.html')


def login(request):
    pass
    return render(request, 'login/index.html')


def regist(request):
    if request.method == 'POST':
        # get the input from website
        username = request.POST.get('username')
        password = request.POST.get('password')

        # input check start #TODO
        # if username.strip() and password:
        #     print('aa')

        # create a object of user
        User_ob = models.User()

        # put the username and password in
        User_ob.UserName = username
        User_ob.Password = password

        # save the change to the database
        User_ob.save()
        print(User_ob)#test

        return render(request, 'login/regist.html')
    return render(request, 'login/regist.html')

# def logout(request):
#     pass
#     return redirect("/login/")
