from dateutil.parser import parse
from django.db import models
from django.db.models import Index

from utils.models import BaseModel, IndexableMixin


class Event(IndexableMixin, BaseModel):
    id = models.BigAutoField(
        primary_key=True,
    )
    name = models.CharField(
        max_length=255,
        verbose_name="nome",
    )
    timestamp = models.DateTimeField(
        verbose_name='timestamp',
    )

    class Meta(BaseModel.Meta):
        verbose_name = "evento"
        indexes = [
            Index(fields=['-timestamp', '-id']),
        ]

    @classmethod
    def _index_name(cls):
        return 'events'

    @classmethod
    def _doc_type(cls):
        return 'event'

    @classmethod
    def _parse_search(cls, doc):
        source = doc['_source']
        return {
            'id': int(doc.get('_id')),
            'name': source.get('name'),
            'timestamp': parse(source.get('timestamp')),
        }

    def _to_doc(self):
        return {
            'name': self.name,
            'timestamp': self.timestamp,
            'suggest': self.name,
        }

    @classmethod
    def search(cls, q):
        return super(Event, cls).search(
            body={
                'text': q,
                'completion': {
                    'field': 'suggest',
                }
            },
            suggest=True,
        )

    def __str__(self):
        return self.name

    def __repr__(self):
        return '{} - {}'.format(self.pk, self.name)
