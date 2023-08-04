import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk
import requests
import json

window = tk.Tk()
window.geometry('900x500')
window.title("My Weather App")


def weather():
    try:
        city = search_entry.get()

        url = f"http://api.weatherapi.com/v1/current.json?key=3edb972799044b39a2361955232106&q={city}"
        weather_data = requests.get(url)
        weather_dict = json.loads(weather_data.text)

        wind_data = weather_dict["current"]["wind_kph"]
        humidity_data = weather_dict["current"]["humidity"]
        current_condition = weather_dict["current"]["condition"]["text"]
        pressure_data = weather_dict["current"]["pressure_mb"]

        temp_data = weather_dict["current"]["temp_c"]
        feel_data = weather_dict["current"]["feelslike_c"]
        cond_data = weather_dict["current"]["condition"]["text"]

        time_data = weather_dict["location"]["localtime"]

        wind_info.config(text=wind_data)
        humidity_info.config(text=humidity_data)
        description_info.config(text=current_condition)
        pressure_info.config(text=pressure_data)

        weather_label.config(text="Current Weather")
        temp_label.config(text=(f"{temp_data} °C "))
        feel_label.config(text=(f"Feels Like {feel_data} °C "))
        cond_label.config(text=cond_data)

        localtime_label.config(text=(f"Current Date and Local Time\n{time_data}"))

    except Exception as e:
        messagebox.showerror("Error:", "Invalid Entry")


search_img = ImageTk.PhotoImage(file="search.png")
search_img_label = tk.Label(window, image=search_img)
search_img_label.place(x=5, y=5)

search_entry = tk.Entry(window, font=("Helvetica", 30, "bold"), bg="#404040", fg="white")
search_entry.place(x=34, y=22)

search_icon_img = ImageTk.PhotoImage(file="search icon.png")
search_icon_button = tk.Button(window, image=search_icon_img, cursor="hand2", command=weather)
search_icon_button.place(x=416, y=16)

logo_img = ImageTk.PhotoImage(file="logo.png")
logo_img_label = tk.Label(window, image=logo_img)
logo_img_label.place(x=300, y=100)

box_img = ImageTk.PhotoImage(file="box.png")
box_img_label = tk.Label(window, image=box_img)
box_img_label.place(x=30, y=370)

wind = tk.Label(window, text="WIND", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
wind.place(x=70, y=390)
humidity = tk.Label(window, text="HUMIDITY", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
humidity.place(x=210, y=390)
description = tk.Label(window, text="DESCRIPTION", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
description.place(x=400, y=390)
pressure = tk.Label(window, text="PRESSURE", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
pressure.place(x=650, y=390)

wind_info = tk.Label(window, text="...", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
wind_info.place(x=70, y=425)
humidity_info = tk.Label(window, text="...", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
humidity_info.place(x=210, y=425)
description_info = tk.Label(window, text="...", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
description_info.place(x=400, y=425)
pressure_info = tk.Label(window, text="...", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
pressure_info.place(x=650, y=425)

weather_label = tk.Label(window, font=("Arial", 20, "bold"))
weather_label.place(x=550, y=100)

temp_label = tk.Label(window, font=("Arial", 40, "bold"))
temp_label.place(x=550, y=150)
feel_label = tk.Label(window, font=("Arial", 15, "bold"))
feel_label.place(x=550, y=220)
cond_label = tk.Label(window, font=("Arial", 15, "bold"))
cond_label.place(x=550, y=260)

localtime_label = tk.Label(window, font=("Arial", 15, "bold"))
localtime_label.place(x=40, y=100)

window.mainloop()