from django.shortcuts import render, redirect
from .forms import AddResourceForm
from django.contrib import messages
from .models import Resource

def index(request):
    resources = Resource.objects.all()
    print(resources)
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
