from django.shortcuts import render, redirect
from .forms import RegisterForm
# Create your views here.
def register(response):
    if response.method =="POST":
            print('1')
            form = RegisterForm(response.POST, response.FILES)
            print(form.errors)
            if form.is_valid():
                print('2')
                form.save()
            return redirect("/index")
    else:
            form = RegisterForm()
    return render(response,"register/register.html", {"form":form})


def loging(response):
    return render(response,"registration/login.html")
