
from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from .views import ArticleViewset

router = DefaultRouter()
router.register(r'^articles', ArticleViewset)

urlpatterns = router.urls


