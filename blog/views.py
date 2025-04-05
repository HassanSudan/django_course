from django.shortcuts import render
from blog.models import Category

# Create your views here.
def HomeView(request):
    return render(request, 'blog/home.html')

# display Category list
def CategoryViewList(request):
    cat = Category.objects.order_by('-id')
    context = {
        'categories': cat
    }
    
    return render(request, 'blog/category.html', context)
