from django.contrib import admin

from v1 import models


@admin.register(models.Sample)
class SampleAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
    )

    list_filter = (
        'name',
    )

    search_fields = (
        'name',
    )

    readonly_fields = (
        'id',
        'created_at',
        'updated_at',
    )

    fieldsets = [
        ('Informações', {
            'fields': (
                'id',
                'name',
                'created_at',
                'updated_at',
            )
        }),
    ]
