from django.shortcuts import render
from django.http import HttpResponse
from .models import collab_project
from .forms import CreateNewProject
from django.contrib import messages

# Create your views here.

def index(request):

    ls = collab_project.objects.all()
    return render(request,'project/indivProject.html',{'ls':ls})

def create(request):
   if request.method=="POST":
       form = CreateNewProject(request.POST , request.FILES)
       print(form.errors )
       if form.is_valid():
           messages.success(request, ('Your project has been submitted successsfully'))
           form.save()
       return render(request,'project/create.html',{})
   return render(request,'project/create.html',{})




    # form = CreateNewProject()
    # if request.method=="Post":
    #     form = CreateNewProject(request.POST)
    #     if form.is_valid():
    #         d = collab_project(p_name=p_name,p_desc=p_desc,p_image=p_image,p_part=p_part)
    #         d.save()
    # #         n = form.cleaned_data["p_name"]
    # #         t = collab_project(p_name=n)
    # #         t.save()
    #     return render(request,'project/create.html')
    # #     return HttpResponseRedirect("/%i" %t.id)
    # # else:
    # #     form = CreateNewProject()
    # # return render(request,'project/create.html',{'form':form})
    # return render(request,'project/create.html',{'form':form})
