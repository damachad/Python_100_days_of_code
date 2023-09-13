import smtplib, random, pandas, os
import datetime as dt

MY_EMAIL = "david00smith98@gmail.com"
PASSWORD = "tluxokwuaqyqkspx"
PLACEHOLDER = "[NAME]"

now = dt.datetime.now()
today = (now.month, now.day)
data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(row.month, row.day): row["name"] for (index, row) in data.iterrows()}

if today in birthdays_dict:
    file = random.choice(os.listdir("letter_templates"))
    name = birthdays_dict[today]
    with open(f"letter_templates/{file}", "r") as letter:
        start_letter = letter.read()
    new_letter = start_letter.replace(PLACEHOLDER, name)
    receiving_email = data[data["name"] == name]["email"]
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=receiving_email,
                            msg=f"Subject:Happy Birthday!\n\n{new_letter}")
