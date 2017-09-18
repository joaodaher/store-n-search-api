from utils.serializers import BaseModelSerializer
from v1 import models


class SampleSerializer(BaseModelSerializer):
    class Meta(BaseModelSerializer.Meta):
        model = models.Sample
        fields = (
            'id',
            'name',
        )
