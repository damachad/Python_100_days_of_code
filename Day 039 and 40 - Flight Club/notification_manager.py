from os import environ
import smtplib
from twilio.rest import Client


class NotificationManager:

    def send_notification(self, flight_data):
        client = Client(username=environ["ACCOUNT_SID"], password=environ["AUTH_TOKEN"])
        body = (f"Low price alert! Only £{flight_data['price']} to fly from {flight_data['city_from']}-"
                f"{flight_data['iata_from']} to {flight_data['city_to']}-{flight_data['iata_to']}, "
                f"from {flight_data['date_from']} to {flight_data['date_to']}.")
        if flight_data['via_city'] != "None":
            body += f"\n\nFlight has 1 stop over, via {flight_data['via_city']}."
        client.messages.create(body=body, to=environ["PHONE_NUMBER"], from_=environ["VIRTUAL_PHONE"])

    def send_email(self, receiver_name, receiving_email, flight_data):
        my_email = environ["EMAIL"]
        password = environ["EMAIL_PWD"]
        body = (f"Subject:Low price alert!\n\nHi {receiver_name},\n\nOnly £{flight_data['price']} to fly "
                f"from {flight_data['city_from']}-{flight_data['iata_from']} to {flight_data['city_to']}-"
                f"{flight_data['iata_to']}, from {flight_data['date_from']} to {flight_data['date_to']}.")
        if flight_data['via_city'] != "None":
            body += f"\n\nFlight has 1 stop over, via {flight_data['via_city']}."
        body += "\n\nThank you for your subscription!\n\nDavid's Flight Club"
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=receiving_email,
                                msg=body.encode('utf-8'))

