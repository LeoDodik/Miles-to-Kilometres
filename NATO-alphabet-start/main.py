import tkinter
from tkinter import Button, Entry

window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width=250, height=200)
window.config(padx=20,pady=20)
# Entry widget for user input


def calculator():
    miles = float(miles_input.get())
    km = miles * 1.609
    kilometer_output.config(text=f"{km}")


miles_input = Entry()
miles_input.grid(column=12 , row=12)

# Label widget for displaying text
miles_text = tkinter.Label(text="Miles")
miles_text.grid(column=13, row=12)  # Placing label in the same row as the entry widget

equal_text = tkinter.Label(text="is equal to")
equal_text.grid(column=11,row=13)

kilometer_output = tkinter.Label(text="0")
kilometer_output.grid(column=12,row=13)

km_text = tkinter.Label(text="Km")
km_text.grid(column=13,row=13)


button = Button(text="Calculate",command=calculator)
button.grid(column=12,row=14)
window.mainloop()
