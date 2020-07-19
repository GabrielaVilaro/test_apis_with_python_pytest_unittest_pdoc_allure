'''Test sobre la API de Twitter para practicar diferentes tipos de autenticación, se hace un GET
y se validan los datos, la API se debe solicitar a Twitter en https://developer.twitter.com/'''

import unittest
import requests
import json

__pdoc__ = {}
__pdoc__["TestApiTwitter"] = False


class TestApiTwitter(unittest.TestCase):
    def setUp(self):
        self.header = {"Content-Type": "application/json", "Authorization": "Bearer " +
                                                                            "AAAAAAAAAAAAAAAAAAAAAKBxGAEAAAAAIhCI8Z0oGZgcmxvr0oN2viBl3gg%3DbejKFdDxuK9r4jvxDZ519jqy8CzcNs"
                                                                            "Dgn4QmidaehGG6hNxn53"}
        self.tweet = 'https://api.twitter.com/1.1/search/tweets.json?q=from%3AStevenWilsonHQ&result_type=mixed&count=2'

    def test_api_twitter_with_tweet(self):
        tweet_response = requests.get(self.tweet, headers=self.header)
        json_response = json.loads(tweet_response.text)
        print(json.dumps(json_response, indent=3))
        assert json_response['statuses'][0]['id_str'] == '1282630333343703041'

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
