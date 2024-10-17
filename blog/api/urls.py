from . import views
from rest_framework.routers import DefaultRouter

app_name = "api"

router = DefaultRouter()
router.register("post", views.PostModelViewSet, basename="post")
router.register("category", views.CategoryModelViewset, basename="category")
urlpatterns = router.urls
