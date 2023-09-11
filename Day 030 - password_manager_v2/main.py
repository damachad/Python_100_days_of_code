from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letter_list = [choice(letters) for _ in range(randint(8, 10))]
    symbol_list = [choice(symbols) for _ in range(randint(2, 4))]
    number_list = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = letter_list + symbol_list + number_list
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(index=0, string=password)

    # Automatically copies password to clipboard
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website_input = website_entry.get()
    email_input = username_entry.get()
    password_input = password_entry.get()
    new_data = {
        website_input: {
            "email": email_input,
            "password": password_input,
        }
    }

    if len(website_input) == 0 or len(email_input) == 0 or len(password_input) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website_input, message=f"These are the details entered: \nEmail: {email_input} \n"
                                                        f"Password: {password_input} \nIs it ok to save?")
        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    # Read old data
                    data = json.load(data_file)
                    # Update old data with new data
                    data.update(new_data)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    # Save data to empty file
                    json.dump(new_data, data_file, indent=4)
            else:
                with open("data.json", "w") as data_file:
                    # Save updated data
                    json.dump(data, data_file, indent=4)
            finally:
                website_entry.delete(0, 'end')
                password_entry.delete(0, 'end')


# ------------------------- SEARCH PASSWORD ---------------------------- #


def find_password():
    website = website_entry.get().lower()
    if len(website) == 0:
        messagebox.showinfo(title="Oops", message="Please specify website to search.")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            messagebox.showinfo(title="Oops", message="No Data File Found")
        else:
            data_lower = {site.lower(): value for (site, value) in data.items()}
            if website in data_lower:
                messagebox.showinfo(title=website.capitalize(), message=f"Email: {data_lower[website]['email']}\n"
                                                           f"Password: {data_lower[website]['password']}")
            else:
                messagebox.showinfo(title="Error", message=f"No details for {website} exist.")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="../logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

# Labels
website_lb = Label(text="Website:")
website_lb.config(padx=10, pady=5)
website_lb.grid(row=1, column=0, sticky=E)
username_lb = Label(text="Email/Username:")
username_lb.config(padx=10)
username_lb.grid(row=2, column=0, sticky=E)
password_lb = Label(text="Password:")
password_lb.config(padx=10, pady=5)
password_lb.grid(row=3, column=0, sticky=E)

# Entries
website_entry = Entry(width=33)
website_entry.focus()
website_entry.grid(row=1, column=1)
username_entry = Entry(width=52)
username_entry.insert(0, "example@email.com")
username_entry.grid(row=2, column=1, columnspan=2)
password_entry = Entry(width=33)
password_entry.grid(row=3, column=1)

# Buttons
search = Button(text="Search", width=15, command=find_password)
search.grid(row=1, column=2)
generate = Button(text="Generate Password", command=generate_password)
generate.grid(row=3, column=2)
add = Button(text="Add", width=44, command=save)
add.grid(row=4, column=1, columnspan=2)

window.mainloop()
