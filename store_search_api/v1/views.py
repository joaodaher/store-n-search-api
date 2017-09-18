from rest_framework import viewsets
from rest_framework_extensions.cache.mixins import CacheResponseMixin

from v1 import models, serializers


class SampleViewSet(CacheResponseMixin, viewsets.ModelViewSet):
    queryset = models.Sample.objects.all()
    serializer_class = serializers.SampleSerializer
