from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post, Category, Tag, Friend, Diary, Video
# from .forms import DateForm
from datetime import datetime
import markdown

def post_markdown(post):
    post.content = markdown.markdown(
        post.content,
        extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.toc',
        ],
        safe_mode=True,
        enable_attributes=False,
    )

def index(request):
    posts = Post.objects.filter(status='completed').order_by('-timestamp')
    for post in posts:
        post_markdown(post)
    return render(request, 'blog/index.html', {'posts':posts})

def category(request, name):
    posts = Post.objects.filter(category__name=name, status='completed').order_by('-timestamp')
    for post in posts:
        post_markdown(post)
    return render(request, 'blog/category.html', {'posts':posts, 'name':name, 'archive_type':'category'})

def tag(request, name):
    posts = Post.objects.filter(tags__name=name, status='completed').order_by('-timestamp')
    for post in posts:
        post_markdown(post)
    return render(request, 'blog/tag.html', {'posts':posts, 'name':name, 'archive_type':'tag'})

def post(request, slug):
    post = Post.objects.filter(slug=slug).first()
    post_markdown(post)
    return render(request, 'blog/article.html', {'post': post})

def about(request):
    return render(request, 'blog/about.html')

def message(request):
    return render(request, 'blog/message.html')

def video(request):
    videos = Video.objects.all()
    return render(request, 'blog/video.html', {'videos': videos})

def diary(request):
    diaries = Diary.objects.all().order_by('-timestamp')
    for diary in diaries:
        post_markdown(diary)
    return render(request, 'blog/diary.html', {'diaries': diaries})

def plan(request):
    error = False
    if 'year' in request.POST and 'month' in request.POST and 'day' in request.POST:
        y = request.POST['year']
        m = request.POST['month']
        d = request.POST['day']

        if not y or not m or not d:
            error = True
        else:
            date = y + '-' + m + '-' + d
            return HttpResponseRedirect('/plan/date/' + date + '/')
    return render(request, 'blog/plan.html', {'error': error})

def plan_year(request):
    error = False
    if 'year' in request.POST:
        y = request.POST['year']
        if not y:
            error = True
        else:
            return HttpResponseRedirect('/plan/year/' + y + '/')
    return render(request, 'blog/plan_year.html', {'error': error})

def plan_year_detail(request, year):
    plans = Plan.objects.filter(category__name='Yearly Log', timevalue=year)
    return render(request, 'blog/plan_year.html', {'plans':plans, 'year': year})

def plan_month(request):
    error = False
    if 'year' in request.POST and 'month' in request.POST:
        y = request.POST['year']
        m = request.POST['month']
        if not y or not m:
            error = True
        else:
            month = y + '-' + m
            return HttpResponseRedirect('/plan/month/' + month + '/')
    return render(request, 'blog/plan_month.html', {'error': error})

def plan_month_detail(request, month):
    plans = Plan.objects.filter(category__name='Monthly Log', timevalue=month)
    return render(request, 'blog/plan_month.html', {'plans':plans, 'month': month})

def plan_date(request):
    error = False
    if 'year' in request.POST and 'month' in request.POST and 'date' in request.POST:
        y = request.POST['year']
        m = request.POST['month']
        d = request.POST['date']

        if not y or not m or not d:
            error = True
        else:
            date = y + '-' + m + '-' + d
            return HttpResponseRedirect('/plan/date/' + date + '/')
    return render(request, 'blog/plan_date.html', {'error': error})

def plan_date_detail(request, date):
    plans = Plan.objects.filter(category__name='Daily Log', timevalue=date)
    note = plans.filter(status='-')
    event = plans.filter(status='∘')
    task = plans.filter(status__in=['·','<','>','x'])
    plans = {'task':task,'note':note,'event':event}
    return render(
        request, 'blog/plan_date.html',
        {'plans':plans, 'date': date}
    )
