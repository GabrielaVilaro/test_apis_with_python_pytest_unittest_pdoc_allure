'''Este test realiza un post a la API de Pet Store de Swagger UI'https://petstore.swagger.io/'''

import requests
import json
import unittest
from apis.base_api_pet_store import BaseApiPetStore

__pdoc__ = {}

__pdoc__["TestApiPostPetStore"] = False


class TestApiPostPetStore(unittest.TestCase):

    def setUp(self):
        self.apiBasePetStore = BaseApiPetStore()

    def test_post_api_pet_store(self):
        """Este tests envía un post a la url del pet store y valida sus datos"""

        response = requests.post(self.apiBasePetStore.url, headers=self.apiBasePetStore.headers,
                                 data=self.apiBasePetStore.body)
        json_response = json.loads(response.text)
        print(json.dumps(json_response, indent=3))

        assert response.status_code == 200
        assert json_response['id'] == 501, 'Not match'
        assert json_response['category']['name'] == 'Perros', 'Not match'
        assert json_response['tags'][0]['name'] == 'Rita', 'Not match'

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()