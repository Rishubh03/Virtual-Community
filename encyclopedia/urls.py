from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("wiki/home/", views.index, name="index"),
    path("wiki/<int:id>/", views.entry, name="entry"),
    path("create/", views.create, name="create"),
    path("edit/<int:id>/", views.edit, name="edit"),
    path("wiki/", views.randomPage, name="random")
]
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
