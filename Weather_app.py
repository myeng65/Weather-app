import tkinter as tk
import requests
import time

def getweather(canvas):
    city = textfield.get()
    api = f"https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=3052c1f097da57f770e0164dfedeab81"

    try:
        json_data = requests.get(api).json()

        # ❌ If city not found
        if json_data.get("cod") != 200:
            label1.config(text="City not found ❌")
            label2.config(text="")
            return

        #json_data = requests.get(api).json()
        condition = json_data['weather'][0]['main']
        temp = int(json_data['main']['temp']-273.15)
        min_temp = int(json_data['main']['temp_min']-273.15)
        max_temp = int(json_data['main']['temp_max']-273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']
        timezone_offset = json_data['timezone']
        sunrise = time.strftime("%I:%M:%S %p", time.localtime(json_data['sys']['sunrise'] + timezone_offset))
        sunset = time.strftime("%I:%M:%S %p", time.localtime(json_data['sys']['sunset'] + timezone_offset))
       
        city_name = json_data['name']
        country = json_data['sys']['country']

        final_info = condition + "\n" + str(temp) + "C"
        final_data = "\n" +"Max Temp: " + str(max_temp) + "\n" + "Min Temp: "+ str(min_temp) + "\n" + "Humidity: " + str(humidity) + "\n" +"Wind Speed: " + str(wind) + "\n" + "sunrise: "+ sunrise + "\n" + "sunset: " + sunset
        label1.config(text = final_info)
        label2.config(text = final_data)

    
    except Exception as e:
        label1.config(text="Error fetching data ❗")
        label2.config(text=str(e))    


canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("weather App")

f = ("poppins",15,"bold")
t = ("poppins",35,"bold")

textfield = tk.Entry(canvas,font = t)
textfield.pack(pady = 20)
textfield.focus()
textfield.bind('<Return>', getweather)

# Added Button 👇
btn = tk.Button(canvas, text="Get Weather", font=f, command=lambda: getweather(canvas), bg="#4CAF50", fg="white")
btn.pack(pady=10)

label1 = tk.Label(canvas, font = t)
label1.pack()
label2 = tk.Label(canvas,font = f)
label2.pack()

canvas.mainloop()
