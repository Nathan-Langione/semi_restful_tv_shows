from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Show
# Create your views here.

def index(request):
    context = {
        "all_shows": Show.objects.all()
    }
    return render(request,'index.html', context)

def add_show(request):

    return render(request,'add_show.html')


def create_show(request):
    if request.method=="POST":
        errors = Show.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect("/shows/new")
        else:
            title = request.POST.get('title')
            network = request.POST.get('network')
            release_date = request.POST.get('release_date')
            description= request.POST.get('description')
            new_show = Show.objects.create(title=title,network=network,release_date=release_date,description=description)
            new_show.save()
            return redirect(f"/shows/{new_show.id}")


def view_show(request, show_id):
    one_show = Show.objects.get(id=show_id)
    context = {
        'this_show': one_show
    }
    return render(request,'view_show.html', context)

def edit_show(request, show_id):
    one_show = Show.objects.get(id=show_id)
    context = {
        'this_show': one_show
    }
    return render(request,'edit_show.html', context )

def update_show(request, show_id):
    if request.method=="POST":
        errors = Show.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect(f"/shows/{show_id}/edit")
        else:
            #specify show
            show_to_update = Show.objects.get(id=show_id)
            #update show attirbutes
            show_to_update.title = request.POST.get('title')
            show_to_update.network = request.POST.get('network')
            show_to_update.release_date = request.POST.get('release_date')
            show_to_update.description= request.POST.get('description')
            #save show
            show_to_update.save()
    return redirect(f"/shows/{show_id}")


def destroy_show(request, show_id):
    """ if request.method=="POST": """
    show_to_delete = Show.objects.get(id=show_id)
    show_to_delete.delete()
    return redirect("/shows")