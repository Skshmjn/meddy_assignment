import sys
import requests

# local
from config import NEWS_API_CONFIG
from utils.caching import cache_api
from utils.common import get_error_traceback
from utils.logging import MyLogger

logger = MyLogger()


@cache_api(cache_time_in_seconds=NEWS_API_CONFIG['cache_time_out'])
def news_api(query=None):
    try:
        # prepare request
        parameters = {'apiKey': NEWS_API_CONFIG['api_key'], 'language': "en"}

        if query:
            url = NEWS_API_CONFIG['search']
            parameters['q'] = query
        else:
            url = NEWS_API_CONFIG['general']

        # make request
        response = requests.get(url, params=parameters).json()

        # prepare custom response
        return news_api_custom_response(response)

    except requests.exceptions.RequestException as e:
        error = get_error_traceback(sys, e)
        logger.error_logger("news_api : %s" % error)
        return []


def news_api_custom_response(response):
    data = response.get('articles')

    news = []
    if not data:
        return news

    for article in data:

        # discard article which don't have title and url
        if 'title' and 'url' not in article:
            continue

        article_data = {
            "headline": article['title'],
            "link": article['url'],
            "source": NEWS_API_CONFIG['name']
        }
        news.append(article_data)

    return news
