import tkinter as tk
import requests
from tkinter import messagebox

def get_weather(city):
    api_key = '20ea15bcaecc12d7f16e6f9539615dab'
    api_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    try:
        response = requests.get(api_url)
        data = response.json()
        
        if data["cod"] != "404":
            main = data['main']
            weather_desc = data['weather'][0]['description']
            temp = main['temp']
            wind_speed = data['wind']['speed']
            
            return f"Temperature: {temp}°C\nWeather: {weather_desc.capitalize()}\nWind Speed: {wind_speed} m/s"
        else:
            return "City not found"
    except Exception as e:
        return "Error fetching data"

def show_weather():
    city = city_entry.get()
    if city:
        weather = get_weather(city)
        weather_label.config(text=weather)
    else:
        messagebox.showwarning("Input Error", "Please enter a city name")

root = tk.Tk()
root.title("Weather App")
root.geometry("400x300")

city_label = tk.Label(root, text="Enter City:", font=("Helvetica", 14))
city_label.pack(pady=10)

city_entry = tk.Entry(root, font=("Helvetica", 14))
city_entry.pack(pady=10)

fetch_button = tk.Button(root, text="Get Weather", font=("Helvetica", 14), command=show_weather)
fetch_button.pack(pady=10)

weather_label = tk.Label(root, text="", font=("Helvetica", 14), justify="left")
weather_label.pack(pady=10)

root.mainloop()



