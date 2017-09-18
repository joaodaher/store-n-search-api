from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="criado em",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="última modificação"
    )

    objects = models.Manager()

    class Meta:
        abstract = True
        get_latest_by = 'updated_at'
        ordering = [
            'id',
        ]
