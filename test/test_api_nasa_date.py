import unittest
import requests
import datetime
import json

class TestNasaApi(unittest.TestCase):

    def setUp(self):
        self.Format = "%Y-%m-%d"
        self.BackDay = datetime.date.today() - datetime.timedelta(days=2)
        self.Day = self.BackDay.strftime(self.Format)
        self.api_key = 'RNbDIcUjE81o0zefiEoJ1OaP6FMCBQcCzvUgRvrs'
        self.date = str(datetime.date.today().strftime("%Y-%m-%d"))
        self.hd = 'False'
        self.url = f"https://api.nasa.gov/planetary/apod?api_key={self.api_key}&date={self.Day}&hd={self.hd}"

    def test_api_nasa_get_data_validation(self):
        '''Este test valida los datos traídos de la API de la Nasa'''

        response = requests.request("GET", self.url)
        json_response = json.loads(response.text)
        print(json.dumps(json_response, indent=3))

        assert response.status_code == 200
        assert json_response['copyright'] == "Emmanuel Paoly", 'No coincide'
        assert json_response['date'] == "2020-07-09", 'No coincide'
        assert json_response['url'] == "https://apod.nasa.gov/apod/image/2007/noctilucentNeowisePaoly600h.jpg", \
            'No coincide'
        assert json_response['title'] == "Noctilucent Clouds and Comet NEOWISE", 'No coincide'

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()