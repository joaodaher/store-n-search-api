from django.db import models

from utils.models import BaseModel


class Sample(BaseModel):
    name = models.CharField(
        max_length=255,
        verbose_name="nome",
    )

    class Meta(BaseModel.Meta):
        verbose_name = "amostra"
        verbose_name_plural = "amostras"

    def __str__(self):
        return self.name

    def __repr__(self):
        return '{} - {}'.format(self.pk, self.name)
