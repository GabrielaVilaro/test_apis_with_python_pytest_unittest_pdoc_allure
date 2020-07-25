'''Este test primero genera el token necesario para acceder a la cuenta y traer los datos e imprime el tokwn_type
y el access token, luego trae los datos del usaurio y hace las validaciones la API se debe solicitar a
Twitter en https://developer.twitter.com/'''

import requests
import json
import unittest
from apis.base_api_twitter import BaseApiTwitter

__pdoc__ = {}
__pdoc__["TestApiTwitterAccessToken"] = False


class TestApiTwitterAccessToken(unittest.TestCase):
    def setUp(self):
        self.apiBaseTwitter = BaseApiTwitter()

    def test_get_response_with_token(self):
        '''Este test primero genera el token necesario para acceder a la cuenta y traer los datos e imprime el tokwn_type
        y el access token, luego trae los datos del usaurio y hace las validaciones
        '''

        print(json.dumps(self.apiBaseTwitter.Authorization_response, indent=3))
        header = {"Content-Type": "application/json",
                  "Authorization": "Bearer " + self.apiBaseTwitter.Authorization_response['access_token']}
        tweet_response = requests.get(self.apiBaseTwitter.tweet, headers=header)
        response = json.loads(tweet_response.text)
        print(json.dumps(response, indent=3))
        assert response['statuses'][0]['id_str'] == '1286000604771487746', 'Not match'

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
