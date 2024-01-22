import requests
from os import environ


class DataManager:

    def get_data(self):
        response = requests.get(url=environ["SHEET_ENDPOINT"] + "prices")
        sheet_data = response.json()["prices"]
        return sheet_data

    def get_emails(self):
        response = requests.get(url=environ["SHEET_ENDPOINT"] + "users")
        users_data = response.json()["users"]
        return users_data
