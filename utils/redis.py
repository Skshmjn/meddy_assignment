import sys
import redis as redis

# local
from config import REDIS_URL, REDIS_PORT, REDIS_DB
from .common import get_error_traceback
from .logging import MyLogger

logger = MyLogger()


class Redis:
    @classmethod
    def redis_connection(cls):
        """
        Redis Connection
        """
        try:

            pool = redis.ConnectionPool(
                host=REDIS_URL,
                port=REDIS_PORT,
                db=REDIS_DB
            )

            redis_conn = redis.Redis(connection_pool=pool)

            # Check if the connection is up
            if redis_conn.ping():
                return redis_conn
            else:
                raise Exception('Redis Server is Down')

        except Exception as e:
            error = get_error_traceback(sys, e)
            logger.error_logger("redis_connection : %s" % error)

    def insert_setex(self, key, value, time_out):
        try:
            redis_conn = self.redis_connection()
            redis_conn.setex(key, time_out, value)

        except Exception as e:
            error = get_error_traceback(sys, e)
            logger.error_logger('insert_setex : %s' % error)

    def get_key_value(self, key):
        try:
            redis_conn = self.redis_connection()
            value = redis_conn.get(key)
            if value:
                value = value.decode('utf-8')
            return value
        except Exception as e:
            error = get_error_traceback(sys, e)
            logger.error_logger('get_key_value : %s' % error)