from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.admin.views.decorators import staff_member_required

from .forms import ProjectUploadForm
@staff_member_required
def upload_project(request):
    if request.method == 'POST':
        form = ProjectUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('project_list')  # Redirect to a view that displays projects
    else:
        form = ProjectUploadForm()
    return render(request, 'upload_project.html', {'form': form})
from .models import Project

@staff_member_required
def project_list(request):
    projects = Project.objects.all()
    return render(request, 'project_list.html', {'projects': projects})
from django.contrib.auth.decorators import login_required

@login_required
def explore(request):
    # Fetch projects
    projects = Project.objects.all()
    return render(request, 'explore.html', {'projects': projects})


from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Project

def delete_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    if request.method == 'POST':
        project.delete()
        return redirect('project_list')  # Redirect to the project list page after deletion
    # Handle GET request or invalid request method
    return redirect('project_list')  # Redirect to the project list page if the request method is not POST



from .forms import MynewsForm
from . models import Mynews
@staff_member_required
def upload_mynews(request):
    if request.method == 'POST':
        form = MynewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('mynews_list')  # Redirect to the mynews list page after saving
    else:
        form = MynewsForm()
    return render(request, 'upload_mynews.html', {'form': form})
# def upload_mynews(request):
#     if request.method == 'POST':
#         form = MynewsForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('mynews_list')  # Redirect to a success page
#     else:
#         form = MynewsForm()
#     return render(request, 'upload_mynews.html', {'form': form})

@login_required
def mynews_list(request):
    mynews = Mynews.objects.all()  # Get all Mynews objects
    return render(request, 'mynews_list.html', {'mynews': mynews, 'request': request})

@staff_member_required
def delete_mynews(request, mynews_title):
    if request.user.is_superuser:
        mynews_instance = get_object_or_404(Mynews, title=mynews_title)
        mynews_instance.delete()
        return redirect('mynews_list')
    else:
        # Handle cases where non-admin users attempt to access delete functionality
        # Redirect to an error page or display a message
        return redirect('mynews_list')
    
