from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'home'
urlpatterns = [
    path('', views.HomeView.as_view()),
    path('ejemplo1/', views.EjemploView1.as_view(),name='ejemplo1'),
    path('ejemplo2/', views.EjemploView2.as_view(),name='ejemplo2'),

]
