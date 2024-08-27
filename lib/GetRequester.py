import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content  # this returns the body as bytes
        pass

    def load_json(self):
        # Get the response body and convert it to a Python object (list or dict)
        response_body = self.get_response_body()
        return json.loads(response_body.decode('utf-8'))
        pass