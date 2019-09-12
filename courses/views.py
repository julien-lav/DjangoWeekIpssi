from django.shortcuts import render, redirect
from .forms import CourseForm
from django.contrib import messages
from .models import Course

def index(request):
    courses = Course.objects.filter(teacher=request.user)
    return render(request, 'courses/index.html', {'courses': courses})

def show(request, course_id):
    course = Course.objects.get(id=course_id)
    return render(request, 'courses/show.html', {'course': course})


def add(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)

        if form.is_valid():
            course = form.save(commit=False)
            course.teacher = request.user
            course.save()

            url = form.cleaned_data.get('url')
            messages.success(request, f'course {url} created for {request.user}')
            return redirect('home')
    else:
        form = CourseForm()
    return render(request, 'courses/add.html', {'form': form})


def edit(request, course_id):
    if request.method == 'POST':
        form = CourseForm(request.POST)

        if form.is_valid():
            Course.objects.filter(id=course_id).update(url=form.cleaned_data.get('url'))

            url = form.cleaned_data.get('url')
            messages.success(request, f'course {url} updated for {request.user}')
        return redirect('home')
    else:
        course = Course.objects.get(id=course_id)
        form = CourseForm(instance=course)
    
    return render(request, 'courses/edit.html', {'form': form, 'course_id': course_id})


def delete(request, course_id):
    course = Course.objects.get(id=course_id)
    Course.objects.filter(id=course_id).delete()
    messages.success(request, f'course {course.url} deleted')
    return redirect('home')
