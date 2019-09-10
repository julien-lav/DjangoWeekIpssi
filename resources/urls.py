from django.urls import path
from django.conf.urls import include

from . import views

app_name = 'resources'
urlpatterns = [
    # ex: /resources/
    path('', views.index, name='resources_index'),
    # ex: /resources/add/
    path('add/', views.add, name='resources_add'),
]