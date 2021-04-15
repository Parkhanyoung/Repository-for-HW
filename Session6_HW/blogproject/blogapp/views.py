from django.shortcuts import render, redirect

# Create your views here.

from .models import Article
import time


def index(request):
    dramas = Article.objects.filter(category='drama')
    movies = Article.objects.filter(category='movie')
    programmings = Article.objects.filter(category='programming')
    return render(request, 'index.html', {'dramas': dramas, 'movies': movies, 'programmings': programmings})


def detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    return render(request, 'detail.html', {'article': article})


def new(request):
    if request.method == 'POST':
        print(request.POST)
        new_article = Article.objects.create(
            title=request.POST['title'],
            content=request.POST['content'],
            category=request.POST['category'],
            time=time.strftime('작성시간: %y년 %m월 %d일 %H:%S',
                               time.localtime(time.time()))
        )
        return redirect('detail', article_pk=new_article.pk)

    return render(request, 'new.html')


def drama(request):
    dramas = Article.objects.filter(category='drama')
    return render(request, 'drama.html', {'dramas': dramas})


def movie(request):
    movies = Article.objects.filter(category='movie')
    return render(request, 'movie.html', {'movies': movies})


def programming(request):
    programmings = Article.objects.filter(category='programming')
    return render(request, 'programming.html', {'programmings': programmings})
