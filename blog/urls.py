from django.urls import path
from . import views

# HTTP Request <-> HTTP Response

app_name = 'blog'

urlpatterns = [
    path('post/<int:post_id>/', views.post, name='post'),
    path('post/', views.blog, name='index'),
    path('example/', views.example, name='example'),
]
