import requests
from handlers.logger import logging
import json
class getBcbData():
    
    def __init__(self):
        with open('configs/configs.json', 'r') as file:
            configs = json.load(file)
        self.selic_url = configs['bcb_base_url'] + configs['bsb_selic_endpoint'] 


    def get_brazil_actual_selic(self):

        response = requests.get(self.selic_url)
        if response.status_code == 200:
            self.payload = response.json()
        else:
            logging.error(f"Unable to fetch data from BCB Api, status code were:{response.status_code}")
            
