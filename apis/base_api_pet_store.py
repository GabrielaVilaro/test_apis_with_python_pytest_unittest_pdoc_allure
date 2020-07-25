class BaseApiPetStore:
    def __init__(self, url=f"https://petstore.swagger.io/v2/pet",
                 headers={"Content-Type": "application/json", "accept": "application/json"}, body="""{
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
        }""", body_put="""{
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
        }"""):
        self.url = url
        self.ID = '/501'
        self.url_id = self.url + self.ID
        self.headers = headers
        self.body = body
        self.body_put = body_put
