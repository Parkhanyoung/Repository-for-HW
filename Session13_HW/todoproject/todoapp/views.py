from django.shortcuts import render, redirect
from .models import Todo, Comment, Like, Scrap
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json
# Create your views here.


def home(request):
    todos = Todo.objects.all().order_by('date')

    return render(request, 'home.html', {'todos': todos})


@login_required(login_url='/registration/login')
def new(request):
    if request.method == 'POST':
        new_todo = Todo.objects.create(
            title=request.POST['title'],
            content=request.POST['content'],
            date=request.POST['date'],
            author=request.user
        )
        return redirect('detail', new_todo.pk)

    return render(request, 'new.html')


@login_required(login_url='/registration/login')
def detail(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    my_like = Like.objects.filter(user=request.user)
    my_scrap = Scrap.objects.filter(user=request.user)
    if request.method == 'POST':
        Comment.objects.create(
            todo=todo,
            content=request.POST['content'],
            author=request.user,
        )
        return redirect('detail', todo_pk)

    return render(request, 'detail.html', {'todo': todo, 'my_like': my_like, 'my_scrap': my_scrap})


def edit(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)

    if request.method == 'POST':
        Todo.objects.filter(pk=todo_pk).update(
            title=request.POST['title'],
            content=request.POST['content'],
            date=request.POST['date'],
        )
        return redirect('detail', todo_pk)

    return render(request, 'edit.html', {'todo': todo})


def delete(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    todo.delete()

    return redirect('home')


def delete_comment(request, todo_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('detail', todo_pk)


def signup(request):
    if request.method == "POST":
        found_user = User.objects.filter(username=request.POST['username'])
        if len(found_user) > 0:
            error = '?????? ???????????? ??????????????????'
            return render(request, 'registration/signup.html', {'error': error})
        new_user = User.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password'],
            )
        auth.login(request, new_user, backend='django.contrib.auth.backends.ModelBackend')
        return redirect('home')

    return render(request, 'registration/signup.html')


def login(request):
    todos = Todo.objects.all().order_by('date')
    if request.method == 'POST':
        found_user = auth.authenticate(
            username=request.POST['username'],
            password=request.POST['password']
        )
        if found_user == None:
            error = '????????? ?????? ??????????????? ???????????????'
            return render(request, 'registration/login.html', {'error': error})
        else:
            auth.login(request, found_user)
            return render(request, 'home.html', {'todos':todos})

    return render(request, 'registration/login.html')


def logout(request):
    auth.logout(request)

    return redirect('home')

@login_required(login_url='/registration/login')
def mypage(request, user_pk):
    user = User.objects.get(pk=user_pk)
    todos = user.posts.all()
    comments = user.comments.all()
    my_likes = user.likes.all()
    my_scraps = user.scraps.all()
    return render(request, 'mypage.html', {'user': user, 'todos':todos, 'comments':comments, 'my_likes': my_likes, 'my_scraps': my_scraps})
    
@csrf_exempt
def like(request):
    if request.method == 'POST':
        request_body = json.loads(request.body) #request.body(string, detail.html?????? stringif?????? ????????????)??? dict??? ??????
        todo_pk = request_body['todo_pk']#request_body?????? dict?????? todo_pk??? value??? ?????????
        print('todopk',todo_pk)

        existing_like = Like.objects.filter(
            todo = Todo.objects.get(pk=todo_pk),
            user = request.user
            )
        # ????????? ?????? ?????? ??????
        if existing_like.count() > 0:
            existing_like.delete()
        
        # ????????? ?????? ????????? ??????
        else:
            Like.objects.create(
                todo = Todo.objects.get(pk=todo_pk),
                user = request.user,
            )
        
        todo_likes = Like.objects.filter(
                todo = Todo.objects.get(pk=todo_pk)
        ) #queryset??????

        response = {
            'like_count': todo_likes.count()
        } #dict??????

        return HttpResponse(json.dumps(response))#dict??? string?????? ????????? ?????????


@csrf_exempt
def scrap(request):
    if request.method == 'POST':
        request_body = json.loads(request.body) #request.body(string, detail.html?????? stringif?????? ????????????)??? dict??? ??????
        todo_pk = request_body['todo_pk']#request_body?????? dict?????? todo_pk??? value??? ?????????
        existing_scrap = Scrap.objects.filter(
            todo = Todo.objects.get(pk=todo_pk),
            user = request.user
            )
        # ????????? ?????? ?????? ??????
        if existing_scrap.count() > 0:
            existing_scrap.delete()
        
        # ????????? ?????? ????????? ??????
        else:
            Scrap.objects.create(
                todo = Todo.objects.get(pk=todo_pk),
                user = request.user,
            )
        
        todo_scraps = Scrap.objects.filter(
                todo = Todo.objects.get(pk=todo_pk)
        ) #queryset??????

        response = {
            'scrap_count': todo_scraps.count()
        } #dict??????

        return HttpResponse(json.dumps(response))#dict??? string?????? ????????? ?????????




