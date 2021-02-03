from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post, Category, Tag, Friend, Diary, Video, PlanCategory, Plan
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
    categories = PlanCategory.objects.all()
    plans = {}
    for category in categories:
        category_plans = Plan.objects.filter(category__name=category).order_by('timestamp')
        plans[category] = category_plans
    return render(request, 'blog/plan.html', {'categories':categories, 'plans': plans})
