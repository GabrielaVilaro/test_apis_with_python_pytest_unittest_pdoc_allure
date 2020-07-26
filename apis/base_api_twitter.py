import json

import requests


class BaseApiTwitter:
    def __init__(self):
        self.header = {"Content-Type": "application/json", "Authorization": "Bearer " +
                                                                            "AAAAAAAAAAAAAAAAAAAAAKBxGAEAAAAAIhCI8Z0oGZgcmxvr0oN2viBl3gg%3DbejKFdDxuK9r4jvxDZ519jqy8CzcNs"
                                                                            "Dgn4QmidaehGG6hNxn53"}
        self.tweet = 'https://api.twitter.com/1.1/search/tweets.json?q=from%3AStevenWilsonHQ&result_type=mixed&count=2'
        self.api_key = "8HRTI5U2gFOhJbNqOPqyw2Fjl"
        self.api_secret = "Z068HodLUjbfOQytarJ62L6Svxx0dzGCEvgr2wHwf4StBpZSiF"
        self.url = "https://api.twitter.com/oauth2/token"
        self.body = {"grant_type": "client_credentials"}
        self.tweet = 'https://api.twitter.com/1.1/search/tweets.json?q=from%3AStevenWilsonHQ&result_type=mixed&count=2'
        self.response = requests.post(self.url, auth=(self.api_key, self.api_secret), data=self.body)
        self.Authorization_response = json.loads(self.response.text)
        self.header = {"Content-Type": "application/json",
                  "Authorization": "Bearer " + self.Authorization_response['access_token']}
