
from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from .views import ArticleView

urlpatterns = [
    url(r'^articles', ArticleView.as_view()),
]


