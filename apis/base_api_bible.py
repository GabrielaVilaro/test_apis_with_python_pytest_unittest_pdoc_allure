class BaseApiBible:
    def __init__(self):
        self.api_key = 'ded0add2b4cdc90d9a529ece52fa986b'
        self.new_header = {'apis-key': self.api_key}
        self.url = f"https://api.scripture.api.bible/v1/bibles"
