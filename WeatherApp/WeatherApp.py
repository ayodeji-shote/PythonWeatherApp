from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

# Dimentions for the weather app
root = Tk()
root.title("Weather Application")
root.geometry("800x600+300+200")
root.resizable(False, False)


def getWeatherdata():
        city = textfield.get()
        geolocator = Nominatim(user_agent="geoapiExercises")
        location = geolocator.geocode(city)
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I:%M: %p")
        clock.config(text=current_time, fg="#4da6ff")
        name.config(text="CURRENT WEATHER", fg="#4da6ff")
        clock.place(x=30, y=400)
        name.place(x=30, y=450)

        # api that the weather service will use
        weatherapi = "https://api.openweathermap.org/data/2.5/weather?q=" + \
            city+"&appid=30d2a3219ee92f2819345457d5143439"
        json_data = requests.get(weatherapi).json()
        condition = json_data["weather"][0]['main']
        description = json_data["weather"][0]['description']
        temp = int(json_data["main"]["temp"]-273.15)
        pressure = json_data["main"]["pressure"]
        humidty = json_data["main"]['humidity']
        wind = json_data["wind"]['speed']
        t.config(text=("Temprature", temp, "°"))
        c.config(text=(condition, "|", "FEELS", "LIKE", temp, "°"))
        w.config(text=(wind, "km/h"))
        w.place(x=60, y=530)
        h.config(text=(humidty, "%"))
        h.place(x=260, y=530)
        d.config(text=(description))
        d.place(x=470, y=530)
        p.config(text=(pressure, "hPa"))
        p.place(x=660, y=530)
# The search bar 
Search=PhotoImage(file="icons/search.png")
Searchimage = Label(image=Search)
Searchimage.place(x=140,y=20)
# The texxt box for the search bar 
textfield = tk.Entry(root,justify="center",width = 15, font=("arial",25,"bold"), bg="#404040",border=0,fg="white")
textfield.place(x=165,y=40)

# Search icon for the search bar
SearchIcon = PhotoImage(file="icons/search_icon.png")
iconimage = Button(image=SearchIcon,borderwidth=0,cursor="hand2",bg="#404040",activebackground="#404040",border=0, command = getWeatherdata)
iconimage.place(x=500,y=33)

# Weather logo for the app
LogoIcon = PhotoImage(file="icons/logo.png")
Logoimage = Label(image=LogoIcon)
Logoimage.place(x=240,y=100)


# Detials box 
box = PhotoImage(file="icons/box.png")
bottombox = Label(image=box)
bottombox.pack(padx=5,pady=5,side=BOTTOM)

# Time 
name = Label(root, font=("arial",15,"bold"))
name.place(x=30,y=100)
clock = Label(root, font=("arial",20))
clock.place(x=30,y=100)
# Details box label 
windlabel = Label(root,text="Wind",font=("Arial",15,"bold"),fg="white",bg="#1ab5ef")
windlabel.place(x=60,y=505)
Huminidtylabel = Label(root,text="Huminidty",font=("Arial",15,"bold"),fg="white",bg="#1ab5ef")
Huminidtylabel.place(x=240,y=505)
Descriptionlabel = Label(root,text="Description",font=("Arial",15,"bold"),fg="white",bg="#1ab5ef")
Descriptionlabel.place(x=460,y=505)
Pressurelabel = Label(root,text="Pressure",font=("Arial",15,"bold"),fg="white",bg="#1ab5ef")
Pressurelabel.place(x=660,y=505)

t = Label(font=("Arial",20,"bold"),fg="#4da6ff")
t.place(x=520,y=400)
c = Label(font=("Arial",15,"bold"),fg="#4da6ff")
c.place(x=520,y=450)
# The text in the wind,humidity,description and pressure section 
w= Label (text="...", font=("Arial",15,"bold"),bg="#1ab5ef")
w.place(x=75,y=530)
h= Label (text="...", font=("Arial",15,"bold"),bg="#1ab5ef")
h.place(x=280,y=530)
d= Label (text="...", font=("Arial",15,"bold"),bg="#1ab5ef")
d.place(x=505,y=530)
p= Label (text="...", font=("Arial",15,"bold"),bg="#1ab5ef")
p.place(x=700,y=530)


root.mainloop()