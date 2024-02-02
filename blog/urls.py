from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.BlogList.as_view(), name='blog_list'),
    path('blog/', views.Blog.as_view(), name='blog'),
]
