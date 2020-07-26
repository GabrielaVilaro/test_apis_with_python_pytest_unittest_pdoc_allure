'''Este test hace a través de un GET, las validaciones de la respuesta a la llamada a la API de la biblia
https://bibliaapi.com/docs/
'''

import unittest
import requests
import json
from apis.base_api_bible import BaseApiBible

__pdoc__ = {}
__pdoc__["TestBible"] = False


class TestBible(unittest.TestCase):

    def setUp(self):
        self.apiBible = BaseApiBible()

    def test_api_bible_data_validation(self):
        '''Este tests verifica , a través de un GET, los datos ID, nameLocal y language, e imprime el Json con la
        respuesta'''

        response = requests.get(url=self.apiBible.url, headers=self.apiBible.new_header)
        json_response = json.loads(response.text)
        print(json.dumps(json_response, indent=3))
        assert response.status_code == 200
        assert json_response['data'][0]['id'] is not None, "Is empty"
        assert json_response['data'][0]['language']['nameLocal'] == 'Nend'
        print(json_response['data'][0]['id'], json_response['data'][0]['language']['nameLocal'])

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
