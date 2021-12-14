import random
from django import forms
from django.shortcuts import redirect, render, get_object_or_404
from encyclopedia.models import Articles
from . import util
from markdown2 import Markdown
from .forms import Search, Post, Edit


markdowner = Markdown()


def index(request):
    articles = Articles.objects.all()

    if request.method == "POST":
        form = Search(request.POST)
        if form.is_valid():
            item = form.cleaned_data["item"]

            queryset = Articles.objects.filter(title__icontains=item)
            context = {
                'searched': queryset,
                'form': Search()
            }
            return render(request, "encyclopedia/search.html", context)

        else:
            return render(request, "encyclopedia/index.html", {"form": form})

    return render(request, "encyclopedia/index.html", {
       "form": Search(), "articles": articles,
    })


def entry(request, id):
    instance = Articles.objects.get(id = id)
           
    context = {
            'articles':instance,
            'form': Search()
        }

    return render(request, "encyclopedia/entry.html", context)
    # else:
    #     return render(request, "encyclopedia/error.html", {"message": "The requested page was not found.", "form": Search()})


def create(request):

    if request.method == 'POST':
        form_data = Post(request.POST, request.FILES)
        if form_data.is_valid():                    
            form_data.save()
            print('done')           
            return redirect(to='index')
    
    return render(request, "encyclopedia/create.html", {"form": Search(), "post": Post()})


def edit(request,id):
    articles = Articles.objects.get(id=id)
    if request.method == 'POST':
        form = Edit(request.POST,instance=articles)        
        if form.is_valid():
            form.save()
          
            return redirect(to='index')
    
    form = Edit(instance = articles)
    context = {
        'form': Search(),
        'edit':form,
        'articles':articles,
    }
        
    return render(request, "encyclopedia/edit.html", context)


def randomPage(request):
    if request.method == 'GET':
        articles = Articles.objects.order_by('?').first()
        
        context = {
            'form': Search(),
            'articles': articles,
        }

        return render(request, "encyclopedia/entry.html", context)
