'''Este test hace a través de un GET, las validaciones de la respuesta a la llamada a la API de la nasa
https://api.nasa.gov/
'''

import unittest
import requests
import datetime
import json
from apis.base_api_nasa import BaseNasaApi

__pdoc__ = {}
__pdoc__["TestNasaApi"] = False


class TestNasaApi(unittest.TestCase):

    def setUp(self):
        self.apiNasa = BaseNasaApi()

    def test_api_nasa_get_data_validation(self):
        '''Este tests valida los datos traídos de la API de la Nasa'''

        response = requests.request("GET", self.apiNasa.url)
        json_response = json.loads(response.text)
        print(json.dumps(json_response, indent=3))

        assert response.status_code == 200
        assert json_response['copyright'] == "Stephane Guisard", 'Not match'
        assert json_response['date'] == "2020-07-23", 'Not match'
        assert json_response['url'] == "https://apod.nasa.gov/apod/image/2007/SGUNeuschwansteinNeowiseIMG2532-1050.jpg", \
            'Not match'
        assert json_response['title'] == "Fairytale NEOWISE", 'Not match'

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
