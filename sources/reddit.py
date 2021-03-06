import sys
import requests

# local
from config import REDDIT_CONFIG
from utils.caching import cache_api
from utils.common import get_error_traceback
from utils.logging import MyLogger

logger = MyLogger()


@cache_api(cache_time_in_seconds=REDDIT_CONFIG['cache_time_out'])
def reddit(query=None):
    try:
        # prepare request
        params = {}

        if query:
            url = REDDIT_CONFIG['search']
            params['q'] = query
        else:
            url = REDDIT_CONFIG['general']

        headers = {'User-agent': 'The Awesome News Aggregator'}

        # create request
        response = requests.get(url=url, params=params, headers=headers).json()

        # prepare response
        return reddit_custom_response(response)

    except requests.exceptions.RequestException as e:
        print('Redis connection failed')
        error = get_error_traceback(sys, e)
        logger.error_logger("reddit_api : %s" % error)
        return []


def reddit_custom_response(response):
    data = response.get('data', {}).get('children', [])

    news = []
    if not data:
        return news

    for article in data:
        article = article.get('data', {})

        # discard article which don't have title and url
        if 'title' and 'url' not in article:
            continue

        article_data = {
            "headline": article['title'],
            "link": article['url'],
            "source": REDDIT_CONFIG['name']
        }
        news.append(article_data)

    return news



