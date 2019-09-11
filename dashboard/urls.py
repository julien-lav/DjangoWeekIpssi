from django.urls import path
from django.conf.urls import include


from . import views

app_name = 'dashboard'
urlpatterns = [
    # ex: /dashboard/
    path('', views.index, name='index'),
    path('create_graph', views.create_graph, name='create_graph'),
    path('graph', views.graph, name='graph'),
    path('custom_graph', views.custom_graph, name='custom_graph')
]
