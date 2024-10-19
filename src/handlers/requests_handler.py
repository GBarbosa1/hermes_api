import requests
from handlers.logger import logging

class apiCall:

    def get(self,url):
        response = requests.get(url)

        if response.status_code == 200:

            self.payload = response.json()
            
        else:
            logging.error(f"Unable to fetch data from {url}, status code were:{response.status_code}")
    