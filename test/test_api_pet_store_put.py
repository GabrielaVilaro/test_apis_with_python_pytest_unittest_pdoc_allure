import requests
import json
import unittest


class TestApiPetStorePut(unittest.TestCase):

    def setUp(self):
        self.url = f"https://petstore.swagger.io/v2/pet"
        self.headers = {"Content-Type": "application/json", "accept": "application/json"}
        self.body = """{
          "id": 10,
          "category": {
            "id": 3,
            "name": "Conejo Malo"
          },
          "name": "Bod Conejito",
          "photoUrls": [
            "https://i.ytimg.com/vi/SfLV8hD7zX4/maxresdefault.jpg",
            "url2"
          ],
          "tags": [
            {
              "id": 1,
              "name": "tag3"
            },
            {
              "id": 2,
              "name": "tag4"
            }
          ],
          "status": "available"
        }"""

    def test_api_pet_store_put(self):
        """Este test hace un put a la url, cmabiando el nombre de la mascota"""

        response = requests.put(self.url, headers=self.headers, data=self.body)
        json_response = json.loads(response.text)
        print(json.dumps(json_response, indent=3))

        assert json_response['id'] is not None, "Esta Vacío"
        assert json_response['category']['name'] == "Conejo Malo", 'No coincide'
        assert json_response['category']['id'] == 3, 'No coincide'

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()