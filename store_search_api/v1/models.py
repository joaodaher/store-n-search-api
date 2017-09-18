from django.db import models
from django.db.models import Index

from utils.models import BaseModel


class Event(BaseModel):
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

    def __str__(self):
        return self.name

    def __repr__(self):
        return '{} - {}'.format(self.pk, self.name)
