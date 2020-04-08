# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 20:47:39 2020

@author: Aviral Gaur
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 16:50:35 2020

@author: Aviral Gaur
"""

import json
import requests
import tkinter as tk
from tkinter import messagebox
from tkinter import *



def createWidgets():
    
    cityLabel = Label(root, text="ENTER CITY NAME : ", bg="skyblue")
    cityLabel.grid(row=0, column=0, padx=10, pady=5)
    cityEntry = Entry(root, width=36, textvariable=cityName)
    cityEntry.grid(row=0, column=1, padx=10, pady=5)
    
    findButton = Button(root, text="FIND WEATHER", command=findWeather)
    findButton.grid(row=1, column=0, padx=10, pady=5, columnspan = 2)
    
    clearButton = Button(root, text="CLEAR", command=clearEntries)
    clearButton.grid(row=1, column=1, padx=10, pady=5, columnspan = 2)
    
    cityCoord = Label(root, text="CITY COORDINATES :", bg="skyblue")
    cityCoord.grid(row=2, column=0, padx=10, pady=5)
    root.cityCoord = Entry(root, width=36)
    root.cityCoord.grid(row=2, column=1, padx=10, pady=5)
    
    tempLabel = Label(root, text="TEMPERATURE :", bg="skyblue")
    tempLabel.grid(row=3, column=0, padx=10, pady=5)
    root.tempEntry = Entry(root, width=36)
    root.tempEntry.grid(row=3, column=1, padx=10, pady=5)
    
    humidityLabel = Label(root, text="HUMIDITY :", bg="skyblue")
    humidityLabel.grid(row=4, column=0, padx=10, pady=5)
    root.humidityEntry = Entry(root, width=36)
    root.humidityEntry.grid(row=4, column=1, padx=10, pady=5)
    
    windLabel = Label(root, text="WIND :", bg="skyblue")
    windLabel.grid(row=5, column=0, padx=10, pady=5)
    root.windEntry = Entry(root, width=36)
    root.windEntry.grid(row=5, column=1, padx=10, pady=5)
    
    pressureLabel = Label(root, text="ATMOSPHERIC PRESSURE :", bg="skyblue")
    pressureLabel.grid(row=6, column=0, padx=10, pady=5)
    root.pressureEntry = Entry(root, width=36)
    root.pressureEntry.grid(row=6, column=1, padx=10, pady=5)
    
    descLabel = Label(root, text="WEATHER DESCRIPTION :", bg="skyblue")
    descLabel.grid(row=7, column=0, padx=10, pady=5)
    root.descEntry = Entry(root, width=36)
    root.descEntry.grid(row=7, column=1, padx=10, pady=5)
    


def findWeather():
    root.cityCoord.delete(0, END)
    root.tempEntry.delete(0,END)
    root.humidityEntry.delete(0,END)
    root.windEntry.delete(0,END)
    root.pressureEntry.delete(0,END)
    root.descEntry.delete(0,END)
    
    
    
    APIkey = "675cafd6b55f614a3feed8e60cc48778"
    
    weatherURL = "https://api.openweathermap.org/data/2.5/weather?"
    cityname = cityName.get()
    
    requestURL = weatherURL+"appid="+APIkey+"&q="+cityname+"&units=metric"
    response = requests.get(requestURL)
    
    weatherResponse = response.json()
    print(json.dumps(weatherResponse, indent=2))
    
    
    if weatherResponse["cod"] != "404":
        
        weatherPARA = weatherResponse["main"]
        coordinates = weatherResponse["coord"]
        latitude = str(coordinates["lat"])
        longitude = str(coordinates["lon"])
        wind = weatherResponse["wind"]
        windspeed = str(wind["speed"])
        
        if 'deg' in wind.keys():
            windDirect = str(wind["deg"])
            
        else:
            windDirect = ''
        temperature = str(weatherPARA["temp"])
        pressure = str(weatherPARA["pressure"])
        humidity = str(weatherPARA["humidity"])
        weatherDesc = weatherResponse["weather"]
        weatherDescription = weatherDesc[0]["description"]
        print(type(temperature))
        #showing the result in tkinter window
        root.cityCoord.insert('0', "LATITUDE : "+latitude+"  LONGITUDE : "+longitude)
        root.tempEntry.insert('0',temperature+" °C")
        root.humidityEntry.insert('0',str(humidity)+" %")
        root.windEntry.insert('0',"SPEED : " +windspeed+" met/sec "+" DIRECTION : "+windDirect+"°")
        root.pressureEntry.insert('0',str(pressure)+" hPa")
        root.descEntry.insert('0',weatherDescription)
                        
    else:
        messagebox.showerror("ERROR"," CITY NOT FOUND!")

    
          
    
def clearEntries():
    cityName.set('')
    root.cityCoord.delete(0, END)
    root.tempEntry.delete(0,END)
    root.humidityEntry.delete(0,END)
    root.windEntry.delete(0,END)
    root.pressureEntry.delete(0,END)
    root.descEntry.delete(0,END)
    
root = tk.Tk()
root.iconbitmap("weather.ico")
root.title("City Weather")
root.config(background='skyblue')
root.geometry("580x330")
root.resizable(False, False)

cityName = StringVar()
createWidgets()

root.mainloop()    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    