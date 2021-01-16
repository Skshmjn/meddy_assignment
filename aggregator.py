from sources.news_api import news_api
from sources.reddit import reddit

value = [news_api, reddit]


def aggregate_news(search_query=None):
    agg_news = []
    for source in value:
        agg_news += source(search_query)
    return agg_news
