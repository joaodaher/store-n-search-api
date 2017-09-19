from rest_framework.routers import DefaultRouter

from v1 import views

router = DefaultRouter()

router.register(r'events', views.EventViewSet)

urlpatterns = router.urls
