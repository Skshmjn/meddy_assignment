import time
from timeit import default_timer as timer

import requests

from unittest import TestCase

from aggregator import aggregate_news
from config import REDDIT_CONFIG, NEWS_API_CONFIG
from utils.caching import cache_api
from utils.redis import Redis


class AppTest(TestCase):
    API_URL = 'http://127.0.0.1:8000'

    def test_home(self):
        r = requests.get('{}'.format(self.API_URL))
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.json(), {
            "CONNECTED": "YOU ARE CONNECTED TO NEWS AGGREGATOR"
        })

    def test_news(self):
        r = requests.get('{}/news'.format(self.API_URL))
        self.assertEqual(r.status_code, 200)

    def test_news_query(self):
        query = 'India'
        r = requests.get('{}/news?q={}'.format(self.API_URL, query))
        self.assertEqual(r.status_code, 200)


class RedisTest(TestCase):

    def test_redis_conn(self):
        redis_client = Redis().redis_connection()
        self.assertEqual(redis_client.ping(), True)

    def test_setex(self):
        redis_setex = Redis().insert_setex('test', 'test_value', 1000)
        self.assertEqual(redis_setex, True)

    def test_get_key_value(self):
        value = Redis().get_key_value('test')
        print(value)
        self.assertEqual(value, 'test_value')


class CachingTest(TestCase):
    @staticmethod
    @cache_api()
    def sample_fun(num):
        time.sleep(3)
        return num

    def test_caching_decorator(self):
        # actual response and calculating actual time
        actual_start = timer()
        actual_response = self.sample_fun(5)
        actual_end = timer()

        # cached response and calculating cached time
        cached_start = timer()
        cached_response = self.sample_fun(5)
        cached_end = timer()

        # actual and cached time
        actual_time = actual_end - actual_start
        cached_time = cached_end - cached_start

        self.assertEqual(actual_response, cached_response)
        self.assertGreater(actual_time, cached_time)


class AggregatorTest(TestCase):

    def test_aggregator_news(self):
        aggregated_news = aggregate_news()

        for news in aggregated_news:
            self.assertIn('headline', news)
            self.assertIn('link', news)
            self.assertIn('source', news)
            self.assertIn(news['source'], [REDDIT_CONFIG['name'], NEWS_API_CONFIG['name']])
