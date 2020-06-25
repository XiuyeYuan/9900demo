from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.shortcuts import redirect
from . import models


#functions to check the input and interact with database
def index(request):
    if request.method == 'POST':
        #get the info from POST request
        username = request.POST.get('username')
        password = request.POST.get('password')
        #create user object
        user_ob = models.User.objects.get(UserName=username)
        #TODO 判空

        if user_ob.Password == password:
            #password right login success!
            return render(request, 'login/loginsuccess.html')
        else:
            #password wrong login fail!
            return render(request, 'login/loginfail.html')
    return render(request, 'login/index.html')


def login(request):
    pass
    return render(request, 'login/index.html')


def regist(request):
    if request.method == 'POST':
        # get the input from website
        username = request.POST.get('username')
        password = request.POST.get('password')

        # input check start #TODO 判空
        # if username.strip() and password:
        #     print('aa')

        # create a object of user
        User_ob = models.User()

        # put the username and password in
        User_ob.UserName = username
        User_ob.Password = password

        # save the change to the database
        User_ob.save()
        print(User_ob)  # test

        return render(request, 'login/regist.html')
    return render(request, 'login/regist.html')

def logout(request):
    pass
    return redirect("/login/")

def loginsuccess(request):
    pass
    return redirect("/loginsuccess/")

def loginfail(request):
    pass
    return redirect("/loginfail/")
