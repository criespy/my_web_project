from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='homepage'),
    path('about-me/', views.AboutMe.as_view(), name='about-me'),
    path('portfolio/', views.Portfolio.as_view(), name='portfolio'),
    path('blog/', views.Blog.as_view(), name='blog'),
]