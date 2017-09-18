from rest_framework.routers import DefaultRouter

from v1 import views

router = DefaultRouter(trailing_slash=False)

router.register(r'samples', views.SampleViewSet)

urlpatterns = router.urls
