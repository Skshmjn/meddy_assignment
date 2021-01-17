import json
import os
from unittest import TestCase

from sources.reddit import reddit, reddit_custom_response


class TestReddit(TestCase):

    def test_reddit(self):
        response = reddit()
        self.assertIsNotNone(response)

    def test_reddit_with_query(self):
        response = reddit(query='bitcoin')
        self.assertIsNotNone(response)

    def test_news_api_custom_response(self):
        file_path = os.path.join(os.path.dirname(__file__), 'reddit.json')
        with open(file_path) as f:
            response = json.load(f)
        response = reddit_custom_response(response)
        expected = [{
            'headline': 'Capitol Police arrested a man with an ‘unauthorized’ inauguration credential and a gun at a security checkpoint.',
            'link': 'https://www.nytimes.com/2021/01/16/us/politics/man-arrested-dc-checkpoint.html',
            'source': 'reddit'}, {'headline': "'Baked Alaska' arrested in Capitol Hill riot: FBI",
                                  'link': 'https://www.reuters.com/article/idUSKBN29L0RN',
                                  'source': 'reddit'},
            {'headline': 'Judge drops charges against 28 Black Lives Matter protesters in Detroit',
             'link': 'https://www.metrotimes.com/news-hits/archives/2021/01/15/judge-drops-charges-against-28-black-lives-matter-protesters-in-detroit',
             'source': 'reddit'},
            {'headline': 'Capitol rioter known as "QAnon Shaman" will be jailed until trial',
             'link': 'https://www.cbsnews.com/news/jake-angeli-qanon-shaman-jail-triial-capitol-riots/',
             'source': 'reddit'}, {
                'headline': 'FBI arrests former U.S. soldier in alleged plot to carry out violence at Florida Capitol',
                'link': 'https://www.tallahassee.com/story/news/local/2021/01/15/capitol-riots-florida-protests-violence/4175324001/',
                'source': 'reddit'}, {'headline': 'Seattle Police responding to incident near FBI building',
                                      'link': 'https://komonews.com/news/local/seattle-police-responding-to-incident-near-fbi-building',
                                      'source': 'reddit'}, {
                'headline': 'A former White supremacist store and Ku Klux Klan meeting space is being turned into a community center to promote healing',
                'link': 'https://www.cnn.com/2021/01/16/us/kkk-museum-redneck-store-echo-project-trnd/index.html',
                'source': 'reddit'}, {'headline': 'Former Cleveland school therapist charged in Capitol riot',
                                      'link': 'https://www.nbcnews.com/news/us-news/cleveland-school-therapist-resigns-post-charged-capitol-riot-n1254411',
                                      'source': 'reddit'},
            {'headline': 'Teacher holds class as he is deployed to US Capitol as part of National Guard',
             'link': 'https://www.boston25news.com/news/trending/teacher-holds-class-he-is-deployed-us-capitol-part-national-guard/555LNAR7SNG6VBRAKPCUQN47VU/',
             'source': 'reddit'},
            {'headline': 'Facebook will temporarily stop showing ads for gun accessories and military gear.',
             'link': 'https://www.nytimes.com/2021/01/16/us/politics/facebook-will-temporarily-stop-showing-ads-for-gun-accessories-and-military-gear.html',
             'source': 'reddit'},
            {'headline': 'Hot Pockets recalled over potential glass and plastic contamination',
             'link': 'https://www.cnn.com/2021/01/16/us/hot-pockets-recall-trnd/index.html',
             'source': 'reddit'}, {
                'headline': "Christian denomination tells 'liberal' churches to be extra vigilant inauguration week",
                'link': 'https://www.tennessean.com/story/news/religion/2021/01/16/united-church-christ-tells-churches-vigilant-inauguration-week/4189115001/',
                'source': 'reddit'},
            {'headline': 'The oldest living Marine, a North Carolina woman, has died at age 107',
             'link': 'https://www.cnn.com/2021/01/16/us/marine-north-carolina-woman-died-107-trnd/index.html',
             'source': 'reddit'},
            {'headline': 'Amazon union election to start in February, U.S. labor board says',
             'link': 'https://www.reuters.com/article/technologyNews/idUSKBN29K2BV', 'source': 'reddit'},
            {'headline': 'Journalists prepare for protests where they could be targets',
             'link': 'https://www.pbs.org/newshour/nation/journalists-prepare-for-protests-where-they-could-be-targets',
             'source': 'reddit'}, {'headline': 'Ex-Florida data scientist Rebekah Jones plans to surrender',
                                   'link': 'https://apnews.com/article/fort-lauderdale-florida-coronavirus-pandemic-ron-desantis-us-news-adb00a0c28dd8c41328b718243a14eba',
                                   'source': 'reddit'},
            {'headline': 'Los Angeles becomes first county to hit 1 million Covid-19 cases',
             'link': 'https://www.nbcnews.com/news/us-news/los-angeles-becomes-first-county-hit-1-million-covid-19-n1254498',
             'source': 'reddit'}, {
                'headline': '‘Honest mistake’: Virginia man arrested at DC checkpoint says he forgot about gun in vehicle',
                'link': 'https://www.wokv.com/news/trending/honest-mistake-virginia-man-arrested-dc-checkpoint-forgot-about-gun-vehicle/7ZRLOLGFPFEMLB2USHZNV4YFNY/',
                'source': 'reddit'}, {'headline': 'Thousands of anti-maskers rally in Austria',
                                      'link': 'https://www.straitstimes.com/world/europe/thousands-of-anti-maskers-rally-in-austria',
                                      'source': 'reddit'},
            {'headline': 'March for Life asks its supporters to stay home this year',
             'link': 'https://apnews.com/article/coronavirus-pandemic-f1ee5826ba13aa633c6a8ab0d20d17c8',
             'source': 'reddit'},
            {'headline': "UNRWA 'mistakenly' gave Palestinian kids textbooks calling for jihad",
             'link': 'https://www.jpost.com/arab-israeli-conflict/unrwa-mistakenly-gave-palestinian-kids-textbooks-calling-for-jihad-655619',
             'source': 'reddit'}, {'headline': 'Police probes compromised after computer records deleted',
                                   'link': 'https://www.bbc.co.uk/news/amp/uk-55684320', 'source': 'reddit'},
            {'headline': 'Santa Barbara County Has Highest COVID-19 Spread in California',
             'link': 'https://www.edhat.com/news/santa-barbara-county-has-highest-covid-19-spread-in-california',
             'source': 'reddit'}, {'headline': 'Orphaned rhinos find refuge in S Africa sanctuary',
                                   'link': 'https://www.aljazeera.com/amp/gallery/2021/1/12/in-pictures-orphaned-rhinos-find-refuge-in-s-africa-sanctuary',
                                   'source': 'reddit'},
            {'headline': '6 suspects in MI Governor Whitmer kidnapping plot set to stand trial in March',
             'link': 'https://www.freep.com/story/news/local/michigan/2021/01/15/gov-whitmer-kidnap-suspects-set-stand-trial-march/4178558001/',
             'source': 'reddit'}]

        self.assertEqual(response, expected)
