from django.urls import path, re_path 
from .views import home, post, category
urlpatterns = [
    path('home/', home,name = 'blog-home'),
    path('blog/<slug:url>', post ,name='post'),
    path('category/<slug:url>', category,name = 'category')
]
