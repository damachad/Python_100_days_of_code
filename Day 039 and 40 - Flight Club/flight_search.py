import requests
from os import environ


class FlightSearch:

    def get_iata(self, city):
        endpoint = "https://api.tequila.kiwi.com/locations/query"
        headers = {
            "Content-Type": "application/json",
            "apikey": environ["API_KEY"],
        }
        params = {
            "term": city,
        }

        response = requests.get(url=endpoint, headers=headers, params=params)
        iata = response.json()["locations"][0]["code"]
        return iata

    def update_iatas(self):
        params = {
            "price": {
                "iataCode": "",
            }
        }
        destinations_data = requests.get(url=environ["SHEET_ENDPOINT"] + "prices").json()["prices"]
        i = 1
        for city in destinations_data:
            i += 1
            try:
                iata = city["iataCode"]
            except KeyError:
                params["price"]["iataCode"] = self.get_iata(city["city"])
                requests.put(url=environ["SHEET_ENDPOINT"] + "prices/" + str(i),
                             json=params)
            else:
                if iata == "":
                    params["price"]["iataCode"] = self.get_iata(city["city"])
                    requests.put(url=environ["SHEET_ENDPOINT"] + "prices/" + str(i),
                                 json=params)

