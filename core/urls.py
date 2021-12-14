from django.contrib import admin
from django.urls import path,include, re_path


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^oauth/', include('social_django.urls', namespace='social')),
    path('',include('users.urls')),
    path('forum/',include('forum.urls')),
    path('blogs/',include('blog.urls')),
    path('',include('encyclopedia.urls')),
    
]
