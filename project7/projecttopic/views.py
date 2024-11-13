from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect 
from.models import Project 
from.forms import ProjectForm

def showproject(request): 
    if request.method == 'POST':
        form =ProjectForm(request.POST) 
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/success')
    else: 
        form = ProjectForm()

    p=Project.objects.all() 
    return render(request, 'show_project.html',{'form': form, 'projects': p})

def success(request): 
    return render(request, 'success.html')