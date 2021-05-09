from django.shortcuts import render, redirect
from .models import Plan
# Create your views here.


def home(request):
    plans = Plan.objects.all()

    return render(request, 'home.html', {'plans': plans})


def new(request):
    if request.method == 'POST':
        plan = Plan.objects.create(
            title=request.POST['title'],
            content=request.POST['content']
        )

        return redirect('detail', plan.pk)

    return render(request, 'new.html')


def detail(request, plan_pk):
    plan = Plan.objects.get(pk=plan_pk)

    return render(request, 'detail.html', {'plan': plan})


def edit(request, plan_pk):
    plan = Plan.objects.get(pk=plan_pk)

    if request.method == 'POST':
        Plan.objects.filter(pk=plan_pk).update(
            title=request.POST['title'],
            content=request.POST['content']
        )
        return redirect('detail', plan_pk)

    return render(request, 'edit.html', {'plan': plan})


def delete(request, plan_pk):
    plan = Plan.objects.get(pk=plan_pk)

    plan.delete()

    return redirect('home')
