from django.shortcuts import render
from django.http import HttpResponse
from .models import collab_project
from .forms import CreateNewProject, SearchForm
from django.contrib import messages
from django.db.models import Q

# Create your views here.


def empty(request):
    return redirect('index/')


def index(response):
    return render(response, 'project/index.html')


def create(request):
    if request.method == "POST":
        form = CreateNewProject(request.POST, request.FILES)
        print(form.errors)
        if form.is_valid():
            messages.success(request,
                             ('Your project has been submitted successsfully'))
            form.save()
        return render(request, 'project/create.html', {})
    return render(request, 'project/create.html', {})


def discover(response):
    ls = collab_project.objects.all()
    return render(request, 'project/indivProject.html', {'ls': ls})


def search_results(request):
    projects = collab_project.objects.all()
    form = SearchForm(request.GET)
    if form.is_valid():
        if form.cleaned_data['q']:
            projects = projects.filter(
                Q(p_name__icontains=form.cleaned_data['q'])
                | Q(p_desc__icontains=form.cleaned_data['q'])
                | Q(p_prerequisite__icontains=form.cleaned_data['q'])
                | Q(p_level__icontains=form.cleaned_data['q'])
                | Q(p_category__icontains=form.cleaned_data['q']))
    return render(
        request, 'project/search-results.html', {
            'searchQuery': form.cleaned_data['q'],
            'project_list': projects,
            'numResults': len(projects)
        })

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
