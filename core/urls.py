from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('users.urls')),
    path('forum/',include('forum.urls')),
    path('blogs/',include('blog.urls')),
    path('',include('encyclopedia.urls')),
]
