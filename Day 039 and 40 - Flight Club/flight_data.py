import requests
import datetime
from os import environ


class FlightData:

    def __init__(self, city_from_iata):
        self.price = 0
        self.real_date_from = datetime.datetime.now().strftime("%d/%m/%Y")
        self.real_date_to = datetime.datetime.now().strftime("%d/%m/%Y")
        self.via_city = "None"

        self.params = {
            "fly_from": city_from_iata,
            "fly_to": "",
            "date_from": datetime.datetime.now().strftime("%d/%m/%Y"),
            "date_to": (datetime.datetime.now() + datetime.timedelta(days=6 * 30)).strftime("%d/%m/%Y"),
            "nights_in_dst_from": 6,
            "nights_in_dst_to": 27,
            "curr": "GBP",
            "max_stopovers": 0,
        }

    def format_date(self, date):
        return date.split("T")[0]

    def get_flight_price(self, fly_to):
        endpoint = "https://api.tequila.kiwi.com/v2/search"
        headers = {
            "Content-Type": "application/json",
            "apikey": environ["API_KEY"],
        }
        self.params["fly_to"] = fly_to
        response = requests.get(url=endpoint, params=self.params, headers=headers)
        try:
            trip_data = response.json()["data"][0]
        except IndexError:
            self.params["max_stopovers"] = 1
            response = requests.get(url=endpoint, params=self.params, headers=headers)
            try:
                trip_data = response.json()["data"][0]
            except IndexError:
                return "No flights available"
            else:
                self.via_city = trip_data["route"][0]["cityTo"]
                self.price = trip_data["price"]
                self.real_date_from = self.format_date(trip_data["local_departure"])
                self.real_date_to = self.format_date(trip_data["route"][2]["local_departure"])
                return self.price
        self.price = trip_data["price"]
        self.real_date_from = self.format_date(trip_data["local_departure"])
        self.real_date_to = self.format_date(trip_data["route"][1]["local_departure"])
        return self.price

