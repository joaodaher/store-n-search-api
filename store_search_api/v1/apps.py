import logging

from django.apps import AppConfig
from django.conf import settings

from elasticsearch import Elasticsearch

logger = logging.getLogger(__name__)


def get_elasticsearch_conn():
    try:
        config = getattr(settings, 'ELASTICSEARCH', {})
        return Elasticsearch(hosts=config.get('HOST', None))
    except:
        logger.error('Unable to contact Elasticsearch')


ES_CONN = get_elasticsearch_conn()


class V1Config(AppConfig):
    name = 'v1'
    verbose_name = "Versão 1"

    def ready(self):
        from v1 import signals    # noqa
