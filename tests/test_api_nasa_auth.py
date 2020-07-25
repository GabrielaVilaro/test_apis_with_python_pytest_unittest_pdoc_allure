'''Este test hace a través de un GET, las validaciones de la respuesta a la llamada a la API de la nasa
https://api.nasa.gov/
'''

import requests
import json
import unittest
from apis.base_api_nasa import BaseNasaApi

__pdoc__ = {}
__pdoc__["TestApiNasaTwo"] = False


class TestApiNasaTwo(unittest.TestCase):

    def setUp(self):
        self.apiNasa = BaseNasaApi()

    def test_api_nasa_date_validation_response(self):
        '''Este tests valida los datos traídos de la API de la Nasa'''

        response = requests.request("GET", self.apiNasa.url_two)
        json_response = json.loads(response.text)
        print(json.dumps(json_response, indent=3))

        assert response.status_code == 200
        assert json_response['links']['next'] == 'http://www.neowsapp.com/rest/v1/feed?start_date=2020-07-20&end_date=2020-07-20&detailed=false&api_key=YnzlCuLqw7MXZV1Sn9QJP5jgycwu25Rskj5LAHSK'
        assert json_response['links']['prev'] == 'http://www.neowsapp.com/rest/v1/feed?start_date=2020-07-18&end_date=2020-07-18&detailed=false&api_key=YnzlCuLqw7MXZV1Sn9QJP5jgycwu25Rskj5LAHSK'
        assert json_response['links']['self'] == 'http://www.neowsapp.com/rest/v1/feed?start_date=2020-07-19&end_date=2020-07-19&detailed=false&api_key=YnzlCuLqw7MXZV1Sn9QJP5jgycwu25Rskj5LAHSK'
        assert json_response['near_earth_objects']['2020-07-19'][0]['links']['self'] == 'http://www.neowsapp.com/rest/v1/neo/3745588?api_key=YnzlCuLqw7MXZV1Sn9QJP5jgycwu25Rskj5LAHSK'

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
