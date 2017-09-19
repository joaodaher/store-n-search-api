from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from utils.views import HealthCheck
from v1.urls import urlpatterns as v1_urls


router = DefaultRouter()

urlpatterns = [
    url(r'^healthcheck/', HealthCheck.as_view()),

    url(r'^', include(router.urls)),
    url(r'^v1/', include(v1_urls)),
]
