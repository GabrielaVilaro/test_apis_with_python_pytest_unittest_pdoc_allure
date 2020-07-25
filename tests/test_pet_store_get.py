'''Este test realiza un GET a la API de Pet Store de Swagger UI'https://petstore.swagger.io/
URL: https://petstore.swagger.io/v2/pet/2 y valida los datos'''

import requests
import json
import unittest
from tests.test_api_pet_store_post import TestApiPostPetStore
from apis.base_api_pet_store import BaseApiPetStore

__pdoc__ = {}
__pdoc__["TestPetStoreGet"] = False


class TestPetStoreGet(unittest.TestCase):
    """Pre- requisitos: Se debe correr el test_api_pet_store_post previamente"""

    def setUp(self):
        self.apiBasePetStore = BaseApiPetStore()

    def test_api_petstore(self):
        '''Este tests verifica, a través del método GET, que los datos que devuelve la petición a la apis sean
        correctos'''

        response = requests.get(self.apiBasePetStore.url_id)
        json_response = json.loads(response.text)
        print(json.dumps(json_response, indent=3))

        assert response.status_code == 200
        assert json_response['id'] == 501, 'Not match'
        assert json_response['name'] == 'Luna', 'Non match'
        assert json_response['category']['name'] == 'Perros', 'Not match'

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
