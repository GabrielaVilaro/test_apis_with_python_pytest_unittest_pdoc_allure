import requests
import json
import unittest


class TestApiPost(unittest.TestCase):

    def setUp(self):
        self.url = f"https://petstore.swagger.io/v2/pet"
        self.headers = {"Content-Type": "application/json", "accept": "application/json"}
        self.body = """{
          "id": 501,
          "category": {
            "id": 3,
            "name": "Perros"
          },
          "name": "Luna",
          "photoUrls": [
            "url1",
            "url2"
          ],
          "tags": [
            {
              "id": 1,
              "name": "Rita"
            },
            {
              "id": 2,
              "name": "Lola"
            }
          ],
          "status": "available"
        }"""

    def test_post_api_pet_store(self):
        """Este test envía un post a la url del pet store y verifica sus datos"""

        response = requests.post(self.url, headers=self.headers, data=self.body)
        json_response = json.loads(response.text)
        print(json.dumps(json_response, indent=3))

        assert json_response['id'] == 501, 'No coincide'
        assert json_response['category']['name'] == 'Perros', 'No coincide'
        assert json_response['tags'][0]['name'] == 'Rita', 'No coincide'

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
