'''Este test primero genera el token necesario para acceder a la cuenta y traer los datos e imprime el tokwn_type
     y el access token, luego trae los datos del usaurio y hace las validaciones la API se debe solicitar a
     Twitter en https://developer.twitter.com/'''

import requests
import json
import unittest

__pdoc__ = {}
__pdoc__["TestApiTwitterAccessToken"] = False

class TestApiTwitterAccessToken(unittest.TestCase):
    def setUp(self):
        self.api_key = "8HRTI5U2gFOhJbNqOPqyw2Fjl"
        self.api_secret = "Z068HodLUjbfOQytarJ62L6Svxx0dzGCEvgr2wHwf4StBpZSiF"
        self.url = "https://api.twitter.com/oauth2/token"
        self.body = {"grant_type": "client_credentials"}
        self.tweet = 'https://api.twitter.com/1.1/search/tweets.json?q=from%3AStevenWilsonHQ&result_type=mixed&count=2'
        self.response = requests.post(self.url, auth=(self.api_key, self.api_secret), data=self.body)
        self.Authorization_response = json.loads(self.response.text)

    def test_get_response_with_token(self):
        '''Este test primero genera el token necesario para acceder a la cuenta y traer los datos e imprime el tokwn_type
        y el access token, luego trae los datos del usaurio y hace las validaciones
        '''

        print(json.dumps(self.Authorization_response, indent=3))
        header = {"Content-Type": "application/json",
                  "Authorization": "Bearer " + self.Authorization_response['access_token']}
        tweet_response = requests.get(self.tweet, headers=header)
        response = json.loads(tweet_response.text)
        print(json.dumps(response, indent=3))
        assert response['statuses'][0]['id_str'] == '1282630333343703041', 'No coincide'

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
