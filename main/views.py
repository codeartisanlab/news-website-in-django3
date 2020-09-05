from django.shortcuts import render
from .models import News, Category
def home(request):
    first_news=News.objects.first()
    three_news=News.objects.all()[1:3]
    three_categories=Category.objects.all()[0:3]
    return render(request,'home.html',{
        'first_news':first_news,
        'three_news':three_news,
        'three_categories':three_categories
    })

# All News
def all_news(request):
    all_news=News.objects.all()
    return render(request,'all-news.html',{
        'all_news':all_news
    })

# Detail Page
def detail(request,id):
    news=News.objects.get(pk=id)
    category=Category.objects.get(id=news.category.id)
    rel_news=News.objects.filter(category=category).exclude(id=id)
    return render(request,'detail.html',{
        'news':news,
        'related_news':rel_news
    })

# Fetch all category
def all_category(request):
    cats=Category.objects.all()
    return render(request,'category.html',{
        'cats':cats
    })


# Fetch all category
def category(request,id):
    category=Category.objects.get(id=id)
    news=News.objects.filter(category=category)
    return render(request,'category-news.html',{
        'all_news':news,
        'category':category
    })

