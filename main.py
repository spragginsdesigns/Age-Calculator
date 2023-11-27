import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import ttkthemes as tkt


def calculate_age():
    try:
        name = name_entry.get()
        birth_year = int(year_entry.get())
        birth_month = int(month_entry.get())
        birth_day = int(day_entry.get())
        birthdate = datetime(birth_year, birth_month, birth_day)
        today = datetime.today()
        age = (
            today.year
            - birthdate.year
            - ((today.month, today.day) < (birthdate.month, birthdate.day))
        )
        messagebox.showinfo("Age", f"{name}'s current age is: {age} years old.")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid date values.")
    except Exception as e:
        messagebox.showerror("Error", str(e))


def change_theme(event):
    selected_theme = theme_combobox.get()
    root.set_theme(selected_theme)


# Set up the themed tkinter window
root = tkt.ThemedTk()

root.title("Age Calculator")
root.geometry("400x300")  # Initial size of the window

# Dropdown menu for theme selection
# label for the combobox
ttk.Label(root, text="Choose theme:").grid(row=0, column=0, padx=10, pady=10)

available_themes = root.get_themes()
theme_combobox = ttk.Combobox(root, values=available_themes, state="readonly")
theme_combobox.bind("<<ComboboxSelected>>", change_theme)
theme_combobox.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
theme_combobox.set("radiance")

# Creating a frame for inputs and button
frame = ttk.Frame(root)
frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

# Configure the grid layout
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(1, weight=1)
frame.grid_columnconfigure(1, weight=1)

# Labels and Entries inside the frame
labels = ["Name:", "Year (YYYY):", "Month (MM):", "Day (DD):"]
for idx, label in enumerate(labels):
    ttk.Label(frame, text=label).grid(row=idx, column=0, padx=10, pady=5, sticky="w")
    entry = ttk.Entry(frame)
    entry.grid(row=idx, column=1, padx=10, pady=5, sticky="ew")

name_entry, year_entry, month_entry, day_entry = (
    frame.grid_slaves(row=0, column=1)
    + frame.grid_slaves(row=1, column=1)
    + frame.grid_slaves(row=2, column=1)
    + frame.grid_slaves(row=3, column=1)
)

# Calculate Button
calculate_button = ttk.Button(frame, text="Calculate Age", command=calculate_age)
calculate_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

# Run the application
root.mainloop()
