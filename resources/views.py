from django.shortcuts import render, redirect
from .forms import AddResourceForm, EditResourceForm
from django.contrib import messages
from .models import Resource

def index(request):
    resources = Resource.objects.filter(user=request.user)
    return render(request, 'index.html', {'resources': resources})


def add(request):
    if request.method == 'POST':
        form = AddResourceForm(request.POST)

        if form.is_valid():
            resource = form.save(commit=False)
            resource.user = request.user
            resource.save()

            url = form.cleaned_data.get('url')
            messages.success(request, f'Resource {url} created for {request.user}')
            return redirect('home')
    else:
        form = AddResourceForm()
    return render(request, 'add.html', {'form': form})


def edit(request, resource_id):
    if request.method == 'POST':
        form = EditResourceForm(request.POST)

        if form.is_valid():
            Resource.objects.filter(id=resource_id).update(url=form.cleaned_data.get('url'))

            url = form.cleaned_data.get('url')
            messages.success(request, f'Resource {url} updated for {request.user}')
        return redirect('home')
    else:
        resource = Resource.objects.get(id=resource_id)
        form = EditResourceForm(instance=resource)
    
    return render(request, 'edit.html', {'form': form, 'resource_id': resource_id})


def delete(request, resource_id):
    resource = Resource.objects.get(id=resource_id)
    Resource.objects.filter(id=resource_id).delete()
    messages.success(request, f'Resource {resource.url} deleted')
    return redirect('home')
