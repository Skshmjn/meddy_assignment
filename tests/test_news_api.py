import json
import os
import unittest

from sources.news_api import news_api, news_api_custom_response


class TestNewsApi(unittest.TestCase):

    def test_news_api(self):
        response = news_api()
        self.assertIsNotNone(response)

    def test_news_api_with_query(self):
        response = news_api(query='bitcoin')
        self.assertIsNotNone(response)

    def test_news_api_custom_response(self):
        file_path = os.path.join(os.path.dirname(__file__), 'news_api.json')
        with open(file_path) as f:
            response = json.load(f)
        response = news_api_custom_response(response)
        expected = [{'headline': 'Bitcoin passes $20k and reaches all-time high',
                     'link': 'http://techcrunch.com/2020/12/16/bitcoin-passes-20k-and-reaches-all-time-high/',
                     'source': 'newsapi'}, {'headline': 'Bitcoin Blows Past $20,000 Milestone',
                                            'link': 'https://gizmodo.com/bitcoin-blows-past-20-000-milestone-1845894176',
                                            'source': 'newsapi'},
                    {'headline': 'Is rising usage driving crypto’s recent price boom?',
                     'link': 'http://techcrunch.com/2020/12/17/is-rising-usage-driving-cryptos-recent-price-boom/',
                     'source': 'newsapi'},
                    {'headline': 'India Weighs 18% Tax on Bitcoin After Legalization of Cryptocurrencies',
                     'link': 'https://gizmodo.com/india-weighs-18-tax-on-bitcoin-after-legalization-of-c-1845960924',
                     'source': 'newsapi'}, {'headline': 'Bitcoin Keeps Moving On Up, Reaching $33,000 in Value',
                                            'link': 'https://gizmodo.com/bitcoin-keeps-moving-on-up-reaching-33-000-in-value-1845979632',
                                            'source': 'newsapi'},
                    {'headline': 'Bitcoin soars past $33,000, its highest ever',
                     'link': 'https://www.cnn.com/2021/01/02/investing/bitcoin-price-30000/index.html',
                     'source': 'newsapi'},
                    {'headline': 'Jack Dorsey defends Twitter’s Trump ban, then enthuses about bitcoin',
                     'link': 'https://www.theverge.com/2021/1/13/22230028/jack-dorsey-donald-trump-twitter-ban-moderation-bitcoin-thread',
                     'source': 'newsapi'},
                    {'headline': "Ripple Claims Bitcoin Is 'Chinese-Controlled' While Announcing New Lawsuit From SEC",
                     'link': 'https://gizmodo.com/ripple-claims-bitcoin-is-chinese-controlled-while-annou-1845932148',
                     'source': 'newsapi'}, {'headline': 'Gemini is launching a credit card with bitcoin rewards',
                                            'link': 'http://techcrunch.com/2021/01/14/gemini-is-launching-a-credit-card-with-bitcoin-rewards/',
                                            'source': 'newsapi'},
                    {'headline': 'Bitcoin hits all-time high rising above $20,000',
                     'link': 'https://www.bbc.co.uk/news/business-55343657', 'source': 'newsapi'},
                    {'headline': 'Bitcoin blasts through $30K - Seeking Alpha',
                     'link': 'https://seekingalpha.com/news/3648183-bitcoin-blasts-through-30k', 'source': 'newsapi'},
                    {'headline': 'Months later, the great Twitter hack still boggles my mind',
                     'link': 'https://www.theverge.com/22163643/twitter-hack-bitcoin-scam-july-2020-elon-musk',
                     'source': 'newsapi'},
                    {'headline': 'Coinbase commits to a “better customer experience” following complaints',
                     'link': 'http://techcrunch.com/2021/01/15/coinbase-commits-to-a-better-customer-experience-following-complaints/',
                     'source': 'newsapi'}, {'headline': 'Bitcoin price passes $20,000, setting new record',
                                            'link': 'https://arstechnica.com/tech-policy/2020/12/bitcoin-price-passes-20000-setting-new-record/',
                                            'source': 'newsapi'},
                    {'headline': "Bitcoin Surges 25% In One Week. Warren Buffett Still Won't Buy It",
                     'link': 'https://news.slashdot.org/story/21/01/03/1844241/bitcoin-surges-25-in-one-week-warren-buffett-still-wont-buy-it',
                     'source': 'newsapi'}, {'headline': 'Bitcoin breaks above $20,000 for first time - Reuters India',
                                            'link': 'https://in.reuters.com/article/crypto-currency-idINKBN28Q1W8',
                                            'source': 'newsapi'},
                    {'headline': 'Bitcoin breaks above $20,000 for first time - Reuters',
                     'link': 'https://www.reuters.com/article/crypto-currency-idUSKBN28Q1UI', 'source': 'newsapi'},
                    {'headline': 'From automation to Bitcoin, Canadian investors see opportunity in 2021 - Reuters UK',
                     'link': 'https://in.reuters.com/article/us-canada-funds-yearend-idINKBN28W1Y0',
                     'source': 'newsapi'},
                    {'headline': 'Bitcoin hits record $28,599.99 as 2020 rally powers on - Reuters',
                     'link': 'https://www.reuters.com/article/crypto-currency-idUSL8N2JA0LE', 'source': 'newsapi'},
                    {'headline': 'Bitcoin Holds Near Record, Ether Surges Amid Crypto Rally - Bloomberg',
                     'link': 'https://www.bloomberg.com/tosv2.html?vid=&uuid=9ec43210-4e6a-11eb-b641-572cf808966a&url=L25ld3MvYXJ0aWNsZXMvMjAyMS0wMS0wNC9ldGhlci1mb2xsb3dzLWJpdGNvaW4tdG8tcmVjb3JkLWhpZ2gtYW1pZC1kaXp6eWluZy1jcnlwdG8tcmFsbHk=',
                     'source': 'newsapi'}]

        self.assertEqual(response, expected)


if __name__ == '__main__':
    unittest.main()
