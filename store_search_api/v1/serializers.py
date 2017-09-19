from utils.serializers import BaseModelSerializer
from v1 import models


class EventSerializer(BaseModelSerializer):
    class Meta(BaseModelSerializer.Meta):
        model = models.Event
        fields = (
            'name',
            'timestamp',
        )
