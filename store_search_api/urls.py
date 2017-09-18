from django.conf.urls import include, url
from django.contrib import admin

from utils.views import HealthCheck
from v1.urls import urlpatterns as v1_urls

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^healthcheck/', HealthCheck.as_view()),

    url(r'^v1/', include(v1_urls)),
]
