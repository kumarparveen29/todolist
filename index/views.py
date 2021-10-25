from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from index.models import List, Task, Contact
from django.contrib import messages

def home(request):
    if request.user.is_anonymous:
        return redirect("/login")
    
    if request.method == "POST":
        heading = request.POST.get('heading')
        Heading = List(name=heading, user=request.user)
        Heading.save()
        return redirect("/")

    context={
        "list" : List.objects.filter(user__username = request.user.username),
        "username": request.user.username,
        "name": request.user.first_name,
        "email": request.user.email
    }
    return render(request, 'home.html', context)

def list(request, title):
    if request.user.is_anonymous:
        return redirect("/login")

    if request.method == "POST":
        new = request.POST.get('new')
        task = Task(name=new, list= List.objects.filter(name=title, user__username = request.user.username).first())
        task.save()

    context={
        "task" : Task.objects.filter(list__name= title, list__user__username = request.user.username),
        "title" : title
    }
    return render(request, 'list.html', context)

def loginuser(request):
    if request.method == "POST":
        username= request.POST.get('username')
        password = request.POST.get('password')
        User= authenticate(username=username, password=password)
        if User is not None:
            login(request, User)
            return redirect("/")
        else:
            messages.error(request, "Wrong username or password")
            return redirect("/login")

    return render(request, 'login.html')

def signupuser(request):
    if request.method == "POST":
        username= request.POST.get('username')
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if len(username)<4 or len(username)>8:
            messages.error(request, "Username must lie between 4 to 8 characters")
            return redirect("/signup")
        for i in range (0,len(User.objects.all())):
            if User.objects.all()[i].username==username:
                messages.error(request, "Username taken")
                return redirect("/signup")
        if len(name)>10:
            messages.error(request, "Name must lie under 10 characters")
            return redirect("/signup")
        if len(password)<5:
            messages.error(request, "Password must be 5 characters atleast")
            return redirect("/signup")


        myuser= User.objects.create_user(username, email, password)
        myuser.set_password(password)
        myuser.first_name = name
        myuser.save()

        username= request.POST.get('username')
        pasword = request.POST.get('password')
        User1= authenticate(username=username, password=password)
        login(request, User1)
        if User is not None:
            return redirect("/")
        else:
            return render("login.html")

    return render(request, 'signup.html')

def logoutuser(request):
    logout(request)
    return redirect('/login')

def delete(request, task, name):
    name = "/list/"+name
    num = Task.objects.filter(name=task, list__user__username = request.user.username)
    num.delete()
    return redirect(name)

def close(request, lst):
    org = List.objects.filter(name=lst, user__username = request.user.username)
    org.delete()
    return redirect("/")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        tel = request.POST.get('tel')
        message = request.POST.get('msg')
        Form = Contact(name=name, tel=tel, message=message, user=request.user)
        Form.save()
        return redirect("/contact")
    return render(request, "contact.html")

def about(request):
    return render(request, "about.html")