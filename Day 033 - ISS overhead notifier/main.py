import requests, smtplib, time
from datetime import datetime

MY_LAT = <your_latitude>
MY_LONG = <your_longitude>
MY_EMAIL = <your_email>
PASSWORD = <your_password>


def send_email():
    # Change the argument based on your email
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL,
                            msg=f"Subject:Look up!\n\nISS passing overhead!")


def is_iss_above_me():
    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()
    iss_data = iss_response.json()

    iss_latitude = float(iss_data["iss_position"]["latitude"])
    iss_longitude = float(iss_data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position.
    if MY_LONG - 5 < iss_longitude < MY_LONG + 5 and \
            MY_LAT - 5 < iss_latitude < MY_LAT + 5:
        return True
    else:
        return False


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    hour_now = datetime.now().hour

    if sunset < hour_now or hour_now < sunrise:
        return True
    else:
        return False


# BONUS: run the code every 60 seconds.
while True:
    time.sleep(60)
    # If the ISS is close to my current position, and it is currently dark
    # Then email me to tell me to look up.
    if is_night() and is_iss_above_me():
        send_email()
