from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework_extensions.cache.mixins import CacheResponseMixin

from v1 import models, serializers


class EventViewSet(CacheResponseMixin, viewsets.ModelViewSet):
    queryset = models.Event.objects.all()
    serializer_class = serializers.EventSerializer

    def list(self, request, *args, **kwargs):
        q = request.query_params.get('q', None)
        if q:
            results = models.Event.search(q=q)
            return Response({
                'results': results,
            })
        else:
            return super(EventViewSet, self).list(request, *args, **kwargs)
