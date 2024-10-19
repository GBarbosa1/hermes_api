import requests
from handlers.logger import logging
from handlers.requests_handler import apiCall
import json
api_operator = apiCall()

class getBcbData():
    
    def __init__(self):
        with open('configs/configs.json', 'r') as file:
            configs = json.load(file)
        self.selic_url = configs['bcb_base_url'] + configs['bcb_selic_endpoint']
        self.inflation_url = configs['bcb_base_url'] + configs['bcb_ipca_endpoint']
        print(self.inflation_url)


    def get_brazil_actual_selic(self):

        response = requests.get(self.selic_url)
        if response.status_code == 200:
            self.payload = response.json()
        else:
            logging.error(f"Unable to fetch data from BCB Api, status code were:{response.status_code}")
            
    def get_brazil_actual_inflation(self):
        api_operator.get(self.inflation_url)
        logging.info(api_operator.payload)
        self.payload = api_operator.payload
        return self.payload 