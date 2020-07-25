'''Test sobre la API de Twitter para practicar diferentes tipos de autenticación, se hace un GET
y se validan los datos, la API se debe solicitar a Twitter en https://developer.twitter.com/'''

import unittest
import requests
import json
from apis.base_api_twitter import BaseApiTwitter

__pdoc__ = {}
__pdoc__["TestApiTwitter"] = False


class TestApiTwitter(unittest.TestCase):
    def setUp(self):
        self.apiBaseTwitter = BaseApiTwitter()

    def test_api_twitter_with_tweet(self):
        tweet_response = requests.get(self.apiBaseTwitter.tweet, headers=self.apiBaseTwitter.header)
        json_response = json.loads(tweet_response.text)
        print(json.dumps(json_response, indent=3))
        assert json_response['statuses'][0]['id_str'] == '1286000604771487746'
        assert json_response['statuses'][0]['id'] == 1286000604771487746
        assert json_response['statuses'][0]['truncated'] == True

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
