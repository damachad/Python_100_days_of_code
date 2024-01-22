from flight_search import FlightSearch
from data_manager import DataManager
from flight_data import FlightData
from notification_manager import NotificationManager

FLY_FROM = "London"
AIRPORT_IATA_FROM = "STN"

Sheet = DataManager()
Search = FlightSearch()
Flights = FlightData(Search.get_iata(FLY_FROM))
Notifier = NotificationManager()

# To get a specific city iata, use Search.get_iata(<city>)
# If necessary, first populate the sheet with city IATAs, using Search.update_iatas()

i = 1
for row in Sheet.get_data():
    i += 1
    code = row["iataCode"]
    if code == "":
        print(f"Unable to access IATA Code. Please update row {i} data")
        continue
    no_data_row = 0
    price = Flights.get_flight_price(fly_to=code)
    if price == "No flights available":
        continue
    elif int(price) < int(row["lowestPrice"]):
        flight_data = {
            "city_from": FLY_FROM,
            "iata_from": AIRPORT_IATA_FROM,
            "city_to": row["city"],
            "iata_to": code,
            "date_from": Flights.real_date_from,
            "date_to": Flights.real_date_to,
            "via_city": Flights.via_city,
            "price": price,
        }
        # Send SMS to designated contact
        # Notifier.send_notification(flight_data=flight_data)

        # Send emails to every user on sheet
        for user in Sheet.get_emails():
            Notifier.send_email(receiver_name=user["firstName"],
                                receiving_email=user["email"],
                                flight_data=flight_data)
