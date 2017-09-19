from django.db import models

from v1.apps import ES_CONN as es


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


class IndexableMixin:
    @classmethod
    def _index_name(cls):
        raise NotImplementedError()

    @classmethod
    def _doc_type(cls):
        raise NotImplementedError()

    @classmethod
    def _parse_search(cls, doc):
        raise NotImplementedError()

    def _to_doc(self):
        raise NotImplementedError()

    def index(self):
        return es.index(
            index=self._index_name(),
            doc_type=self._doc_type(),
            id=self.pk,
            body=self._to_doc(),
        )

    @classmethod
    def search(cls, body, suggest=False, **kwargs):
        if suggest:
            response = es.suggest(
                index=cls._index_name(),
                body={
                    cls._doc_type(): body,
                },
                **kwargs
            )
            try:
                docs = response.get(cls._doc_type())[0].get('options')
                return [cls._parse_search(doc) for doc in docs]
            except TypeError:
                return []

        else:
            return es.search(
                index=cls._index_name(),
                doc_type=cls._doc_type(),
                body=body,
                **kwargs
            )

