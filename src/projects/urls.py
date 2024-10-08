from rest_framework.routers import DefaultRouter

from projects import views

router = DefaultRouter()
router.register(r"all", views.ProjectViewSet)

urlpatterns = router.urls
