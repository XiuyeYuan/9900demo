from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.shortcuts import redirect
from . import models
from django.contrib import messages


# functions to check the input and interact with database
def index(request):
    if request.method == 'POST':
        # get the info from POST request
        username = request.POST.get('username')
        password = request.POST.get('password')

        # try method. in case there is no such a user
        try:
            # create a user instance
            user_ob = models.User.objects.get(UserName=username)
            # check the password

            if user_ob.Password == password:
                # password right login success!
                request.session['username'] = username
                # login success-->userpage.html
                return render(request, 'login/userpage.html', {'username': username})

            else:
                # password wrong login fail!
                messages.error(request, 'Wrong Password')
                return render(request, 'login/index.html')

        except models.User.DoesNotExist:
            messages.error(request, "Wrong Username")
            return render(request, 'login/index.html')

    # method is not 'POST'
    return render(request, 'login/index.html')


def regist(request):
    if request.method == 'POST':
        # get the input from website request
        username = request.POST.get('username')
        password = request.POST.get('password')

        # input check start #TODO 判空

        try:  # check if the user exist
            user_check = models.User.objects.get(UserName=username)  # get the user instance
            if (user_check):  # user exists
                print("Username has been used")
                messages.error(request, "Username has been used")
                return render(request, 'login/regist.html')
        except models.User.DoesNotExist:
            # create a object of user
            User_ob = models.User()

            # put the username and password in
            User_ob.UserName = username
            User_ob.Password = password
            User_ob.save()  # save the change to the database

            # start--create a default collection for each new user
            default_collection = models.Collection()  # create a collection instance
            default_collection.CoName = 'Default'  # a default name for collection
            default_collection.CoOwner = models.User.objects.get(UserId=User_ob.UserId)
            default_collection.save()
            # end--create a default collection for each new user
            return render(request, 'login/index.html')
    return render(request, 'login/regist.html')


def profileview(request):
    if request.method == 'GET':
        username = request.session["username"]
        user_instance = models.User.objects.get(UserName=username)
        collection_instance = models.Collection.objects.filter(CoOwner_id=user_instance.UserId)
        collection_list = []  # a list for multiple collections owned by user
        for collection in collection_instance:
            collection_list.append(collection.CoName)
        return render(request, "login/profile.html", {"username": username, "collection_list": collection_list})


def createcollection(request):
    username = request.session["username"]  # get username from session
    if request.method == "POST":
        collection_name = request.POST.get("Coname")
        User_instance = models.User.objects.get(UserName=username)  # create user instance

        # start --duplication check
        Collections_instance = models.Collection.objects.filter(CoOwner_id=User_instance.UserId)
        collection_list = []
        for ele in Collections_instance or collection_name == 'Defult':
            collection_list.append(ele.CoName)
        if collection_name in collection_list:
            messages.error(request, "Duplicate collection!")  # post a message to inform the user
            return render(request, "login/profile.html", {"username": username, "collection_list": collection_list})
        # end --duplication check

        # start--create new collection
        New_collection_instance = models.Collection()
        New_collection_instance.CoName = collection_name
        New_collection_instance.CoOwner = models.User.objects.get(UserId=User_instance.UserId)
        New_collection_instance.save()
        # end--create new collection

        # create list of collection for return
        Collections_instance = models.Collection.objects.filter(CoOwner_id=User_instance.UserId)
        collection_list = []
        for ele in Collections_instance:
            collection_list.append(ele.CoName)
        return render(request, "login/profile.html", {"username": username, "collection_list": collection_list})

    # create list of collection for return
    User_instance = models.User.objects.get(UserName=username)
    Collections_instance = models.Collection.objects.filter(CoOwner_id=User_instance.UserId)
    collection_list = []
    for ele in Collections_instance:
        collection_list.append(ele.CoName)
    return render(request, "login/profile.html", {"username": username, "collection_list": collection_list})


def deleteCollection(request):
    username = request.session["username"]  # get username from session
    user_instance = models.User.objects.get(UserName=username)  # create user instance
    if request.method == 'POST':
        record = request.POST
        collection_name = list(record.keys())[1]
        if collection_name != 'Default':  # if it is a user-created collection
            models.Collection.objects.get(CoName=collection_name).delete()  # delete operation
            messages.error(request, "Delete Success!")  # post a message to inform the user
            # create list of collection for return
            Collections_instance = models.Collection.objects.filter(CoOwner_id=user_instance.UserId)
            collection_list = []
            for ele in Collections_instance:
                collection_list.append(ele.CoName)
            return render(request, "login/profile.html", {"username": username, "collection_list": collection_list})
        else:  # it is a default collection created when regist
            # create list of collection for return
            Collections_instance = models.Collection.objects.filter(CoOwner_id=user_instance.UserId)
            collection_list = []
            for ele in Collections_instance:
                collection_list.append(ele.CoName)
            messages.error(request, "Can not delete Default collection!")  # post a message to inform the user
            return render(request, "login/profile.html", {"username": username, "collection_list": collection_list})


def logout(request):
    pass
    return redirect("/login/")


def loginsuccess(request):
    pass
    return redirect("/loginsuccess/")


def loginfail(request):
    pass
    return redirect("/loginfail/")


def login(request):
    pass
    return render(request, 'login/index.html')
