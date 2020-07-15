import requests
import json
import unittest


class PetStore(unittest.TestCase):

    def setUp(self):
        self.url = f"https://petstore.swagger.io/v2/pet/2"

    def test_api_petstore(self):
        '''Este tests verifica, a través del método GET, que los datos que devuelve la petición a la api sean
        correctos'''

        response = requests.get(self.url)
        json_response = json.loads(response.text)
        print(json.dumps(json_response, indent=3))

        assert response.status_code == 200
        assert json_response['id'] == 2, 'No coincide'
        assert json_response['name'] == 'John', 'No coincide'
        assert json_response['status'] == 'pending', 'No coincide'
        assert json_response['category']['id'] == 7, 'No coincide'
        assert json_response['category']['name'] == 'John'

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
