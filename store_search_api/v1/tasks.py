from v1.apps import ES_CONN as es


def create_event_mapping():
    index_name = 'events'
    doc_type = 'event'

    event_mapping = {
        'properties': {
            'name': {'type': 'string'},
            'timestamp': {'type': 'date'},
            'suggest': {
                'type': 'completion',
                'analyzer': 'simple',
                'search_analyzer': 'simple',
            }
        }
    }
    body = {
        'mappings': {
            doc_type: event_mapping,
        }
    }

    if es.indices.exists(index=index_name):
        es.indices.delete(index=index_name)

    es.indices.create(
        index=index_name,
        body=body,
    )
