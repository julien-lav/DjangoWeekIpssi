from django.shortcuts import render, redirect
from .forms import ResourceForm
from django.contrib import messages
from .models import Resource


def index(request):
    resources = Resource.objects.filter(teacher=request.user)
    return render(request, 'resources/index.html', {'resources': resources})

def show(request, resource_id):
    resource = Resource.objects.get(id=resource_id)
    return render(request, 'resources/show.html', {'resource': resource})

def add(request):
    if request.method == 'POST':
        form = ResourceForm(request.POST)
        print(form.is_valid())
        if form.is_valid():            
            resource = form.save(commit=False)
            resource.teacher = request.user                            
            
            resource.save()

            url = form.cleaned_data.get('url')

            messages.success(request, f'Resource {url} created for {request.user}')
            return redirect('home')
    else:
        form = ResourceForm()
    return render(request, 'resources/add.html', {'form': form})
    # else:
    #     form = ResourceForm(request.user)
    # return render(request, 'resources/add.html', {'form': form})

def edit(request, resource_id):
    if request.method == 'POST':
        form = ResourceForm(request.POST)

        if form.is_valid():
            Resource.objects.filter(id=resource_id).update(url=form.cleaned_data.get('url'))

            url = form.cleaned_data.get('url')
            messages.success(request, f'Resource {url} updated for {request.user}')
        return redirect('home')
    else:
        resource = Resource.objects.get(id=resource_id)
        form = ResourceForm(instance=resource)
    
    return render(request, 'resources/edit.html', {'form': form, 'resource_id': resource_id})

def delete(request, resource_id):
    resource = Resource.objects.get(id=resource_id)
    Resource.objects.filter(id=resource_id).delete()
    messages.success(request, f'Resource {resource.url} deleted')
    return redirect('home')
