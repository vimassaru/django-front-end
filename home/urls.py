from django.urls import path
from . import views
# HTTP Request <-> HTTP Response

app_name = 'home'

urlpatterns = [
    path('', views.home, name='index'),
]
