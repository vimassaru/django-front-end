from django.contrib import admin
from django.http import HttpResponse
from django.urls import include, path

# HTTP Request <-> HTTP Response


urlpatterns = [
    path('', include('home.urls')),
    path('blog/', include('blog.urls')),
    path('admin/', admin.site.urls),
]
