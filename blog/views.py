from django.shortcuts import render
from blog.models import Category, Post
from django.core.paginator import Paginator

# Create your views here.
def HomeView(request):
    featurePosts = Post.objects.order_by('-id')[:3]
    post_lists = Post.objects.order_by('-id')
    categories = Category.objects.order_by('-id')

    paginator = Paginator (post_lists, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    context = {
        'featurePosts': featurePosts,
        # 'post_lists': post_lists
        'posts': posts,
        'categories': categories
    }
    return render(request, 'blog/home.html', context)

# display Category list
def CategoryViewList(request):
    cat = Category.objects.order_by('-id')
    context = {
        'categories': cat
    }
    
    return render(request, 'blog/category.html', context)
