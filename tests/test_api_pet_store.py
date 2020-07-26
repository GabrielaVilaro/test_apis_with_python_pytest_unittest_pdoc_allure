'''Este test realiza un post, put y get a la API de Pet Store de Swagger UI'https://petstore.swagger.io/'''

import requests
import json
import unittest
from apis.base_api_pet_store import BaseApiPetStore

__pdoc__ = {}

__pdoc__["TestApiPostPetStore"] = False


class TestsApiPetStore(unittest.TestCase):

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

    def test_api_pet_store_put(self):
        """Este tests hace un put a la url, cmabiando el nombre de la mascota
        Este test realiza un PUT a la API de Pet Store de Swagger UI'https://petstore.swagger.io/"""

        response = requests.put(self.apiBasePetStore.url, headers=self.apiBasePetStore.headers,
                                data=self.apiBasePetStore.body_put)
        json_response = json.loads(response.text)
        print(json.dumps(json_response, indent=3))

        assert response.status_code == 200
        assert json_response['id'] is not None, "Is empty"
        assert json_response['category']['name'] == "Conejo Malo", 'Not match'
        assert json_response['category']['id'] == 3, 'Not match'

    def test_api_pet_store_get(self):
        '''Este tests verifica, a través del método GET, que los datos que devuelve la petición a la apis sean
        correctos, Este test realiza un GET a la API de Pet Store de Swagger UI'https://petstore.swagger.io/
        URL: https://petstore.swagger.io/v2/pet/2 y valida los datos
        Pre- requisitos: Se debe correr el test_api_pet_store_post previamente
        '''

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
