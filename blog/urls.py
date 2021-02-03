from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<slug:slug>/', views.post, name='post'),
    path('category/<str:name>/', views.category, name='category'),
    path('tag/<str:name>/', views.tag, name='tag'),
    path('about/', views.about, name='about'),
    path('message/', views.message, name='message'),
    path('video/', views.video, name='video'),
    path('diary/', views.diary, name='diary'),
    path('plan/', views.plan, name='plan'),
]

# from django.views.generic import RedirectView
# urlpatterns += [
#     path('', RedirectView.as_view(url='/catalog/')),
# ]
