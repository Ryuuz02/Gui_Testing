# Using a tutorial Taken from https://realpython.com/python-gui-tkinter/ THIS IS NOT ENTIRELY MY WORK


import tkinter as tk
import tkinter.ttk as ttk
from time import sleep

test_window = tk.Tk()

# legacy_greeting = tk.Label(text="Hello User").pack()
# modern_greeting = ttk.Label(text="Hello User").pack()

expanded_label = tk.Label(
    text="Hello User", 
    bg="#34A2FE",
    fg="white",
    width=10,
    height=15
)
# expanded_label.pack()

button = tk.Button(
    text = "Am button",
    height = 5,
    width = 25,
    bg = "#7897F0",
    fg = "green"
)
# button.pack()

entry_label = tk.Label(
    text = "Enter your name below"
)

name_entry = tk.Entry(
    width = 50
)

name_output = tk.Entry(
)

entry_button = tk.Button(
    text = "Click to read your name",
    command = lambda: name_output.insert(0, name_entry.get())
)
# entry_label.pack()
# name_entry.pack()
# entry_button.pack()
# name_output.pack()

text_box = tk.Text()

# text_box.pack()

def reader_function():
    counter = 0
    idx = 1
    line = ""
    while True:
        sleep(1)
        char = text_box.get(str(idx) + "." + str(counter), str(idx) + "." + str(counter+1))
        if char != "":
            line += char
            counter += 1
        else:
            break
    print(line)


reader_button = tk.Button(
    text = "Read the text box",
    command = reader_function
)
# reader_button.pack()

frame1 = tk.Frame(
    relief=tk.RAISED,
    borderwidth=5
)
frame2 = tk.Frame(
    relief=tk.RIDGE,
    borderwidth=5
)

frame1_label = tk.Label(
    master = frame1,
    text = "I am a label in frame1"
)

frame2_label = tk.Label(
    master = frame2,
    text = "In frame2, I am a label"
)

# frame1_label.pack()
# frame2_label.pack()
# frame1.pack()
# frame2.pack()

lbl1 = tk.Label(
    bg = "red",
    height=20,
    width=20
)

lbl2 = tk.Label(
    bg = "blue",
    height=10,
    width=10
)

lbl3 = tk.Label(
    bg = "green",
    height=5,
    width=5
)

# lbl1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
# lbl2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
# lbl3.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

# lbl1.place(x=0, y=0)
# lbl2.place(x=25, y=25)
# lbl3.place(x=50, y=50)

lbl1.grid(row=0, column=0, padx=0, pady=0)
lbl2.grid(row=1, column=1, padx=5, pady=5)
lbl3.grid(row=2, column=2, padx=10, pady=10)

# Display the window
test_window.mainloop()

