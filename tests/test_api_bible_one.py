import unittest
import requests
import json

class Test01(unittest.TestCase):

    def setUp(self):
        self.api_key = 'ded0add2b4cdc90d9a529ece52fa986b'
        self.new_header = {'api-key': self.api_key}
        self.url = f"https://api.scripture.api.bible/v1/bibles"

    def test_api_bible_data_validation(self):
        '''Este tests verifica , a través de un GET, los datos ID, nameLocal y language, e imprime el Json con la
        respuesta'''

        response = requests.get(self.url, headers=self.new_header)
        json_response = json.loads(response.text)
        print(json.dumps(json_response, indent=3))

        assert response.status_code == 200
        assert json_response['data'][0]['id'] is not None, "El campo esta vacio"
        assert json_response['data'][0]['language']['nameLocal'] == 'Nend'
        print(json_response['data'][0]['id'], json_response['data'][0]['language']['nameLocal'])

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
