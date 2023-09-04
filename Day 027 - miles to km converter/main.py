from tkinter import *
FONT = ("Arial", 16)


def button_clicked():
    miles = int(miles_entry.get())
    kms = round(miles * 1.609344, 2)
    result.config(text=f"{kms}")


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=160, height=100)
window.config(padx=80, pady=50)

# Entry
miles_entry = Entry(width=15)
miles_entry.grid(row=0, column=1)

# Labels
mile_label = Label(text="Miles", font=FONT)
mile_label.grid(row=0, column=2)

equal = Label(text="is equal to", font=FONT)
equal.grid(row=1, column=0)

result = Label(text="0", font=FONT)
result.grid(row=1, column=1)

km = Label(text="Km", font=FONT)
km.grid(row=1, column=2)

# Button
button = Button(text="Calculate", command=button_clicked, font=FONT)
button.grid(row=2, column=1)

window.mainloop()
