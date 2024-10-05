import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import json
import os

DATA_FILE = "bmi_data.json"


if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as f:
        user_data = json.load(f)
else:
    user_data = {}


def save_data(name, weight, height, bmi):
    if name not in user_data:
        user_data[name] = []
    user_data[name].append({"weight": weight, "height": height, "bmi": bmi})
    with open(DATA_FILE, "w") as f:
        json.dump(user_data, f)

def calculate_bmi():
    try:
        name = name_entry.get()
        weight = float(weight_entry.get())
        height = float(height_entry.get()) / 100  
        if height <= 0 or weight <= 0:
            raise ValueError("Height and weight must be positive.")

        bmi = weight / (height * height)
        bmi = round(bmi, 2)

        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obesity"

        result_label.config(text=f"BMI: {bmi} ({category})")
        save_data(name, weight, height, bmi)

    except ValueError as ve:
        messagebox.showerror("Invalid Input", f"Error: {str(ve)}")
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")


def view_history():
    name = name_entry.get()
    if name in user_data:
        bmi_values = [entry["bmi"] for entry in user_data[name]]
        plt.plot(bmi_values, marker="o")
        plt.title(f"BMI History for {name}")
        plt.ylabel("BMI")
        plt.xlabel("Entry Number")
        plt.show()
    else:
        messagebox.showinfo("No Data", f"No data found for {name}")


root = tk.Tk()
root.title("BMI Calculator")


tk.Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=10)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Weight (kg):").grid(row=1, column=0, padx=10, pady=10)
weight_entry = tk.Entry(root)
weight_entry.grid(row=1, column=1, padx=10, pady=10)


tk.Label(root, text="Height (cm):").grid(row=2, column=0, padx=10, pady=10)
height_entry = tk.Entry(root)
height_entry.grid(row=2, column=1, padx=10, pady=10)


calc_button = tk.Button(root, text="Calculate BMI", command=calculate_bmi)
calc_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)


result_label = tk.Label(root, text="")
result_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)


history_button = tk.Button(root, text="View History", command=view_history)
history_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)


root.mainloop()
