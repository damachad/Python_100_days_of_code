# Birthday Wisher 🎉

This project automatically sends birthday wishes to your friends and loved ones. It reads from a CSV file (containing birthdays and contact information) and sends personalized birthday emails using SMTP.

## Features 📋

🍰 Automatically sends birthday wishes via email on the day of the recipient's birthday.   
💌 Personalized messages with customizable templates.   
📅 Easily maintain your contacts in a CSV file.   
🔐 Securely send emails via your Gmail account.   

## Usage 🚀

1. Clone the repository to your local machine.
2. Ensure you have Python installed, along with the required libraries.
3. Modify the MY_EMAIL and PASSWORD variables in the code to include your email and password.
4. Run the `main.py` script, once a day. For optimal use, use a Python automation tool to run this every day at any given time.

## Customization 🛠️

Feel free to customize the template letters in 'letter_templates' to better adjust to your needs. Update the 'birthday.csv' with your contacts info in this format (name, email, year, month, day), with the "year", "month" and "day" refering to the contact's birthday.

## Notes ⚠️

This program will only work if your email is from a Gmail account. If you want to use a different account, you need to update the 'smtplib.SMTP()' call. More info [here](https://docs.python.org/3/library/smtplib.html).
