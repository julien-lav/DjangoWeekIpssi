from django.urls import path
from django.conf.urls import include

from . import views

app_name = 'courses'
urlpatterns = [
    # ex: /courses/
    path('', views.index, name='courses_index'),
    # ex: /courses/1/
    path('<int:course_id>/', views.show, name='courses_show'),
    # ex: /courses/add/
    path('add/', views.add, name='courses_add'),
    # ex: /courses/1/edit/
    path('<int:course_id>/edit/', views.edit, name='courses_edit'),
    # ex: /courses/1/delete/
    path('<int:course_id>/delete/', views.delete, name='courses_delete'),
]