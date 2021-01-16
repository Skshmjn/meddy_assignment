import os

# Logging
DIRECTORY = os.path.join(os.path.abspath(os.getcwd()), 'log')
APP_NAME = "NewsAgg"

# Redis
REDIS_URL = "0.0.0.0"
REDIS_PORT = 6379
REDIS_DB = 0

NEWS_API_KEY = os.environ.get("NEWS_API_KEY",
                              "cf72280b324b4192821203f2616cf646")

REDDIT_CONFIG = {
    'name': 'reddit',
    "general": "https://www.reddit.com/r/news/.json",
    "search": "https://www.reddit.com/r/news/search.json",
    "cache_time_out": 60,

}

NEWS_API_CONFIG = {
    'name': 'newsapi',
    "general": "https://newsapi.org/v2/top-headlines",
    "search": "https://newsapi.org/v2/everything",
    "cache_time_out": 60,
    'api_key': NEWS_API_KEY
}

DEFAULT_API_CACHE_TIME = 60

