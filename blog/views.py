from django.shortcuts import render
from blog.models import Category, Post

# Create your views here.
def HomeView(request):
    featurePosts = Post.objects.order_by('-id')[:3]
    post_lists = Post.objects.order_by('-id')
    context = {
        'featurePosts': featurePosts,
        'post_lists': post_lists
    }
    return render(request, 'blog/home.html', context)

# display Category list
def CategoryViewList(request):
    cat = Category.objects.order_by('-id')
    context = {
        'categories': cat
    }
    
    return render(request, 'blog/category.html', context)
