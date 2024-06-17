import tkinter # for gui
from tkinter import *
import requests # for http request
from tkinter import messagebox  # for using messagebox in tkinter
from PIL import Image,ImageTk # for processing and displaying images
import ttkbootstrap
import time # for time



windows = ttkbootstrap.Window(themename="morph")
windows.title("Weather App")
windows.geometry('550x550')
windows.config(bg="slategray")

# creating function for getting the weather information
# these function will retrive the data from the opennweathermap api and returns into form of weather , city name, country name,wearther discription and a icon

def all_infoweather(area):

    API_KEY = "97826b5632170c69c1b40985a9a09cff"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={area}&appid={API_KEY}"

    # url = f"https://api.openweathermap.org/data/2.5/weather?q={area}&appid={API_KEY}"
    req = requests.get(url)
    if req.status_code == 404:

        messagebox.showerror("Error","City Not Found☹")
        return None

    

     # parse the response Json to get weather information

    weather = req.json()

    # global weather ,image,tempe,info,location_label,country

    try:

        image = weather['weather'][0]['icon']

        tempe = weather['main']['temp'] - 273.15

        info = weather['weather'][0]['description']

        # description

        humidity = weather['main']['humidity']

        windspeed = weather['wind']['speed']

        area =  weather['name']

        country = weather['sys']['country']
        pressure = weather['main']['pressure']  # Pressure in hPa
        sunrise_timestamp = weather['sys']['sunrise']
        sunset_timestamp = weather['sys']['sunset']
        

    except:

        pass

    

   # get the icon url and return all the weather information 

    weather_icon_url = f"https://openweathermap.org/img/wn/{image}@2x.png"

    

    return(weather_icon_url,image,tempe,info,area,country,humidity,windspeed,pressure,sunrise_timestamp, sunset_timestamp)


def convert_timestamp_to_time(timestamp):
   
   

    local_time = time.localtime(timestamp)
    return time.strftime("%H:%M", local_time)  # 24-hour format





def serach():

    area = name.get()
    output = all_infoweather(area)

    if output is None:

        return

    # Getting result

    weather_icon_url,image,tempe,info,area,country,windspeed,humidity,pressure,sunrise_timestamp, sunset_timestamp = output
    area_lebal.config(text=f"{area},{country}")

    

   

 # It's for Weather ICON ,description ,humidity ,windspeed pressure , sunset and sunrise time on display screen

    

    image_res = requests.get(weather_icon_url, stream=True)

    ico_display = Image.open(image_res.raw)

    icon_photo = ImageTk.PhotoImage(ico_display)

    imagelabel.config(image=icon_photo)

    imagelabel.image = icon_photo

    temp.config(text=f"Temperature: {tempe:.2f}°C",background="slategray",foreground="white")

    info_label.config(text=f"Description: {info}",background="slategray",foreground="white")

    hu_label.config(text=f"Humidity:{humidity}%",background="slategray",foreground="white")

    wi_label.config(text=f"Wind Speed:{windspeed} m/s",background="slategray",foreground="white")
    pressure_label.config(text=f"Pressure: {pressure} hPa", foreground="white", background="slategray")

    sunrise_time = convert_timestamp_to_time(sunrise_timestamp)
    sunset_time = convert_timestamp_to_time(sunset_timestamp)

    sunrise_label.config(text=f"Sunrise: {sunrise_time}", foreground="white", background="slategray")
    sunset_label.config(text=f"Sunset: {sunset_time}", foreground="white", background="slategray")

Title = Label(windows,text="Weather App" , bg="slategray" , fg="aquamarine" , font=("futura",20,"bold"))
Title.pack(anchor="center",pady="20px")


La = ttkbootstrap.Label(windows,text="Enter City OR Country Name  ",font=('Times New Roman',17),foreground="white",background="slategray").pack(side="top")

name = ttkbootstrap.Entry(windows,font=('Times New Roman',19),foreground="black",background="slategray")

name.pack(pady=10)



# from display the information 

searchbtn = ttkbootstrap.Button(windows,text="Search",command=serach)

searchbtn.pack(pady=10)





# For enter City or country name

area_lebal = ttkbootstrap.Label(windows,font=('Times New Roman',20),foreground="white",background="slategray")

area_lebal.pack()



# Image

imagelabel = ttkbootstrap.Label(windows)

imagelabel.pack()



# Show temp

temp = Label(windows,foreground="white",font=('Times New Roman',22),background="slategray")
temp.pack(pady=5)

# Weather info

info_label = Label(windows,foreground="white",font=('Times New Roman',18),background="slategray")
info_label.pack(pady=5)



# for humididty

hu_label = Label(windows,font=('Times New Roman',18),foreground="white",background="slategray")
hu_label.pack(pady=5)



# wind 

wi_label = Label(windows,font=('Time new Roman',18),foreground="white",background="slategray")
wi_label.pack(pady=5)



pressure_label = Label(windows, font=('Times New Roman', 18), background="slategray")
pressure_label.pack(pady=5)

sunrise_label = Label(windows, font=('Times New Roman', 18), background="slategray")
sunrise_label.pack(pady=5)

sunset_label = Label(windows, font=('Times New Roman', 18), background="slategray")
sunset_label.pack(pady=5)
windows.mainloop()
