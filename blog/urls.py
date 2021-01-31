from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('message/', views.message, name='message'),
    path('video/', views.video, name='video'),
    path('diary/', views.diary, name='diary'),
    
    path('plan/', views.plan, name='plan'),    
    path('plan/year/', views.plan_year, name='plan_year'),
    path('plan/year/<str:year>/', views.plan_year_detail,
         name='plan_year_detail'),
    path('plan/month/', views.plan_month, name='plan_month'),
    path('plan/month/<str:month>/', views.plan_month_detail,
         name='plan_month_detail'),
    path('plan/date/', views.plan_date, name='plan_date'),
    path('plan/date/<str:date>/', views.plan_date_detail,
         name='plan_date_detail'),
    
    path('post/<slug:slug>/', views.post, name='post'),
    path('category/<str:name>/', views.category, name='category'),
    path('tag/<str:name>/', views.tag, name='tag'),
]

# from django.views.generic import RedirectView
# urlpatterns += [
#     path('', RedirectView.as_view(url='/catalog/')),
# ]
