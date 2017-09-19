from django.db.models.signals import post_save
from django.dispatch import receiver

from v1 import models


@receiver(post_save, sender=models.Event, dispatch_uid="index_event")
def index_event(sender, instance, **kwargs):
    instance.index()
