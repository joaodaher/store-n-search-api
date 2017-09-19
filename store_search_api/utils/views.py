from rest_framework.response import Response
from rest_framework.views import APIView


class HealthCheck(APIView):
    GENERIC_SUCCESS = '\U0001F44D'
    GENERIC_FAIL = '\U0001F44E'

    def get(self, request):
        db = self._check_db()

        server = db.get('healthy')

        return Response(data={
            'db': db,
            'server': {
                'healthy': server,
                'message': self.GENERIC_SUCCESS if server else self.GENERIC_FAIL,
            },
        })

    def _check_db(self):
        from django.db import connections
        from django.db.utils import OperationalError
        db_conn = connections['default']
        try:
            db_conn.cursor()
            healthy = True
            message = self.GENERIC_SUCCESS
        except OperationalError as e:
            healthy = False
            message = str(e)
        return {
            'healthy': healthy,
            'message': message,
        }
