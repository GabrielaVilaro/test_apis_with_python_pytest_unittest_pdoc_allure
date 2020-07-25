'''Este test realiza un PUT a la API de Pet Store de Swagger UI'https://petstore.swagger.io/'''

import requests
import json
import unittest
from apis.base_api_pet_store import BaseApiPetStore

__pdoc__ = {}
__pdoc__["TestApiPetStorePut"] = False


class TestApiPetStorePut(unittest.TestCase):

    def setUp(self):
        self.apiBasePetStore = BaseApiPetStore()

    def test_api_pet_store_put(self):
        """Este tests hace un put a la url, cmabiando el nombre de la mascota"""

        response = requests.put(self.apiBasePetStore.url, headers=self.apiBasePetStore.headers,
                                data=self.apiBasePetStore.body_put)
        json_response = json.loads(response.text)
        print(json.dumps(json_response, indent=3))

        assert response.status_code == 200
        assert json_response['id'] is not None, "Is empty"
        assert json_response['category']['name'] == "Conejo Malo", 'Not match'
        assert json_response['category']['id'] == 3, 'Not match'

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
