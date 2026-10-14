# Weather App:-
# -----------

from tkinter import *
import tkinter as tk

import customtkinter
from geopy.geocoders import Nominatim

from customtkinter import CTkImage
from PIL import Image, ImageTk

from tkinter import messagebox
from timezonefinder import TimezoneFinder

from datetime import datetime, timezone, timedelta
import requests

import pytz

# ================================================================================================    

# Main Window:-
# -----------

root = customtkinter.CTk()
root.title("Weather App")
root.geometry("500x550")
root.resizable(False,False)
root.configure(fg_color="#f8fafc")
# ================================================================================================    

# Header Label:-
# ------------

Header = customtkinter.CTkFrame(
    root,
    height=70,
    fg_color="#7696ff",
    corner_radius=0
)
Header.pack(fill="x")

# ================================================================================================    

# Weather Label:-
# -------------

Weather_label = customtkinter.CTkLabel(
    Header,
    text="Weather App",
    font=("Arial",25, "bold"),
    text_color="white"
)
Weather_label.pack(padx=10, pady=20)

# ================================================================================================    

# Frame:-
# -----

Search_frame = customtkinter.CTkFrame(
    root,
    width=800,
    height=50,
    fg_color="transparent"
)
Search_frame.pack(pady=40)

# ================================================================================================    

# Search Entry Widget:-
# -------------------

Search_label = customtkinter.CTkEntry(
    Search_frame,
    placeholder_text="Location...",
    font=("Arial", 18),
    corner_radius=20,
    width=250,
    height=40
)
Search_label.pack(side=customtkinter.LEFT, fill="x", expand=True, padx=(0, 10))

# Search Button:-
# -------------

btn = customtkinter.CTkButton(
    Search_frame,
    text="Search",
    font=("Arial", 18, "bold"),
    corner_radius=20,
    width=80,
    fg_color="#7696ff",
    text_color="white",
    command=lambda: get_weather()
)
btn.pack(side=customtkinter.RIGHT)

# ================================================================================================    

# Card Frame Container:-
# --------------------

Card_frame = customtkinter.CTkFrame(
    root,
    width=445,
    height=300,
    fg_color="#7696ff",
    corner_radius=20
)
Card_frame.pack(pady=20)
Card_frame.pack_propagate(False)

# ================================================================================================    

# Weather Image:-
# -------------

Weather_image = customtkinter.CTkImage(
    light_image=Image.open(r"C:\Users\HARMEET KAUR\OneDrive\Documents\Gurpreet Folder\Module A1, A2, A3, A4\Python Projects\Weather_App_Python\images\cloudy.png"),
    size=(40,40)
)

# Weather Image Placement:-
# -----------------------

my_label = customtkinter.CTkLabel(
    Card_frame,
    text="",
    image=Weather_image
)
my_label.pack(anchor="nw", padx=20, pady=20)

# ================================================================================================    
    
# Card Content:-
# ------------

# Icon:-
# ----

icon_label = customtkinter.CTkLabel(
    Card_frame,
    text=""
)
icon_label.place(x=40, y=70)

# Temp:-
# ----

temp_label = customtkinter.CTkLabel(
    Card_frame,
    text="--°",
    font=("Arial", 40, "bold"),
    text_color="white"
)
temp_label.place(x=260, y=40)

# Condition:-
# ---------

condition_label = customtkinter.CTkLabel(
    Card_frame,
    text="Condition",
    font=("Arial", 20),
    text_color="white"
)    
condition_label.place(x=260, y=100)

# City:-
# ----

city_label = customtkinter.CTkLabel(
    Card_frame,
    text="City",
    font=("Arial", 18, "bold"),
    text_color="white"
)
city_label.place(x=260, y=130)

# Date:-
# ----

date_label = customtkinter.CTkLabel(
    Card_frame,
    text="Date",
    font=("Arial", 14, "bold"),
    text_color="white",
)
date_label.place(x=260, y=160)

# Time:-
# ----

time_label = customtkinter.CTkLabel(
    Card_frame,
    text="Time",
    font=("Arial", 14),
    text_color="white",
)
time_label.place(x=260, y=190)

# ================================================================================================

# Humidity One:-
# ------------

humidity_one = customtkinter.CTkLabel(
    Card_frame,
    text="Humidity",
    font=("Arial", 13),
    text_color="white",
)
humidity_one.place(x=70, y=260)


# Humidity Label Placement:-
# ------------------------

humidity_label = customtkinter.CTkLabel(
    Card_frame,
    text="",
    font=("Arial", 16, "bold"),
    text_color="white",
)
humidity_label.place(x=70, y=240)


# Humidity Image:-
# --------------

humidity_image = customtkinter.CTkImage(
    light_image=Image.open(r"C:\Users\HARMEET KAUR\OneDrive\Documents\Gurpreet Folder\Module A1, A2, A3, A4\Python Projects\Weather_App_Python\images\humidity.png"),
    size=(30,30)
)

# Humidity Image Placement:-
# ------------------------

humiy_label = customtkinter.CTkLabel(
    Card_frame,
    text="",
    image=humidity_image
)
humiy_label.place(x=20, y=250)

# =================================================================================================

# Wind One:-
# --------

wind_one = customtkinter.CTkLabel(
    Card_frame,
    text="Wind Speed",
    font=("Arial", 13),
    text_color="white",
)
wind_one.place(x=190, y=260)

# Wind Label Placement:-
# --------------------

wind_label = customtkinter.CTkLabel(
    Card_frame,
    text="",
    font=("Arial", 16, "bold"),
    text_color="white",
)
wind_label.place(x=190, y=240)

# Wind Image:-
# ----------

wind_image = customtkinter.CTkImage(
    light_image=Image.open(r"C:\Users\HARMEET KAUR\OneDrive\Documents\Gurpreet Folder\Module A1, A2, A3, A4\Python Projects\Weather_App_Python\images\wind.png"),
    size=(30,30)
)

# Wind Image Placement:-
# --------------------

wind_image_icon = customtkinter.CTkLabel(
    Card_frame,
    text="",
    image=wind_image
)
wind_image_icon.place(x=140, y=250)


# ================================================================================================    

# Visibility One:-
# --------------

Visibility_one = customtkinter.CTkLabel(
     Card_frame,
     text="Visibility",
     font=("Arial", 13),
     text_color="white"
)
Visibility_one.place(x=325, y=260)

# Visibility Label Placement:-
# --------------------------

Visibility_label = customtkinter.CTkLabel(
    Card_frame,
    text="",
    font=("Arial", 16, "bold"),
    text_color="white"
)    
Visibility_label.place(x=325, y=240)    

# Visibility Image:-
# ----------------

Visibility_image = customtkinter.CTkImage(
    light_image=Image.open(r"C:\Users\HARMEET KAUR\OneDrive\Documents\Gurpreet Folder\Module A1, A2, A3, A4\Python Projects\Weather_App_Python\images\visibility.png"),
    size=(30,30)
)

# Visibility Image Placement:-
# --------------------------

Visibility_icon = customtkinter.CTkLabel(
    Card_frame,
    text="",
    image=Visibility_image
)
Visibility_icon.place(x=280, y=250)

# ================================================================================================    

# API & URL :-
# ---------

API_KEY = "f7c8150bece69499e214653f4f993ab6"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"


# API Function:-
# ------------

def get_weather():
    city = Search_label.get()

    if city == "":
        messagebox.showerror("Error!", "Enter city name")
        return

    params = {
        "q":city,
        "appid":API_KEY,
        "units":"metric"}

    try:
        res = requests.get(BASE_URL, params=params)
        data = res.json()
        
        if data["cod"] != 200:
            messagebox.showerror("Error!","City Not Fount")
            return
        
        temp = round(data["main"]["temp"])
        weather = data["weather"][0]["main"]
        icon = data["weather"][0]["icon"]
        humidity = data["main"]["humidity"]
        wind = data["wind"]["speed"]
        visibility = data["visibility"]
       
        
        # timezone:-
        
        tz_offset = data["timezone"]

        city_timezone = timezone(timedelta(seconds=tz_offset))
        city_time = datetime.now(city_timezone)

        formatted_time = city_time.strftime("%I:%M %p")

        now = datetime.now().strftime("%A, %B %d")
        
        # Update Labels:-
        
        temp_label.configure(text=f"{temp}°C")
        condition_label.configure(text=weather)
        city_label.configure(text=city.title())
        date_label.configure(text=now)
        time_label.configure(text=formatted_time)
        humidity_label.configure(text=(humidity,"%"))
        wind_label.configure(text=(wind,"m/s"))
        Visibility_label.configure(text=(visibility, "km"))
        
        # Load icon:-

        load_icon(icon)
        
    except:
        messagebox.showerror("Error","Internet Problem!")

def load_icon(icon_code):
    url = f"http://openweathermap.org/img/wn/{icon_code}@2x.png"
    
    respones = requests.get(url, stream=True)

    with open("icon.png", "wb") as f:
        f.write(respones.content)

    img = Image.open("icon.png")
    
    ctk_img = customtkinter.CTkImage(
        light_image=img,
        dark_image=img,
        size=(140,140)
    )

    icon_label.configure(image= ctk_img)
    icon_label.image =  ctk_img

    
root.mainloop()
print(root)


































