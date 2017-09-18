from rest_framework import viewsets
from rest_framework_extensions.cache.mixins import CacheResponseMixin

from v1 import models, serializers


class EventViewSet(CacheResponseMixin, viewsets.ModelViewSet):
    queryset = models.Event.objects.all()
    serializer_class = serializers.EventSerializer
