from django.urls import path
from .views import upload_project, project_list,upload_mynews,delete_mynews, delete_project, explore, mynews_list

urlpatterns = [
    path('upload_project/', upload_project, name='upload_project'),
    # Add other URL patterns as needed
    path('explore/', explore, name='explore'),
    path('projects/', project_list, name='project_list'),
path('projects/delete/<int:project_id>/', delete_project, name='delete_project'),
#  path('projects/add/', add_project, name='add_project'),
path('upload-mynews/',upload_mynews, name='upload_mynews'),
path('mynews_list/', mynews_list, name='mynews_list'),
path('mynews_list/<str:mynews_title>/delete/', delete_mynews, name='delete_mynews'),

]
