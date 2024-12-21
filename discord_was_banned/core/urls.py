from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about_me/", views.about_me,name="about_me"),
    path("project/", views.project,name="project"),
    path("ya_rabotayu_s/", views.ya_rabotayu_s,name="ya_rabotayu_s"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)