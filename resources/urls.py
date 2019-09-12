from django.urls import path
from django.conf.urls import include

from . import views

app_name = 'resources'
urlpatterns = [
    # ex: /resources/
    path('', views.index, name='resources_index'),
    # ex: /resources/1/
    path('<int:resource_id>/', views.show, name='resources_show'),
    # ex: /resources/add/
    path('add/', views.add, name='resources_add'),
    # ex: /resources/1/edit/
    path('<int:resource_id>/edit/', views.edit, name='resources_edit'),
    # ex: /resources/1/delete/
    path('<int:resource_id>/delete/', views.delete, name='resources_delete'),
]