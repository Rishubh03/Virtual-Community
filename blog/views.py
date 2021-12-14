from django.http import HttpResponse
from django.shortcuts import render
from blog.models import Post, Category


# Create your views here.
def home(request):
    # load all the post from db(10)
    posts = Post.objects.all()[:11]
   

    cats = Category.objects.all()

    data = {
        'posts': posts,
        'cats': cats
    }
    return render(request, 'blog/home.html', data)


def post(request, url):
    post = Post.objects.get(url=url)
    cats = Category.objects.all()

    # print(post)
    return render(request, 'blog/posts.html', {'post': post, 'cats': cats})


def category(request, url):
    cats = Category.objects.all()
    cat = Category.objects.get(url=url)
    posts = Post.objects.filter(cat=cat)
    return render(request, "blog/category.html", {'cats':cats,'cat': cat, 'posts': posts})
