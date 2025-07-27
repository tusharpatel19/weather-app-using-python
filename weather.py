import requests
from tkinter import *

def get_weather():
    city = city_entry.get().strip()
    if "," not in city:
        city = city + ",IN"  # Default to India

    api_key = "62e20e02e71f1e27ae9960a4bad9d32c"  # Replace this
    lang = "en"
    units = "metric"

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&lang={lang}&units={units}"

    try:
        response = requests.get(url)
        data = response.json()

        if data["cod"] == 200:
            temp = data["main"]["temp"]
            description = data["weather"][0]["description"]
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]

            result = (
                f"City: {city.title()}\n"
                f"Temperature: {temp}°C\n"
                f"Weather: {description}\n"
                f"Humidity: {humidity}%\n"
                f"Wind Speed: {wind_speed} m/s"
            )
            result_label.config(text=result)
        else:
            result_label.config(text=f"City not found 😔\n{data.get('message')}")
    except Exception as e:
        result_label.config(text="Error fetching weather ❌")

# GUI Setup
root = Tk()
root.title("Weather App")

city_entry = Entry(root, font=("Arial", 14))
city_entry.pack(pady=10)

get_button = Button(root, text="Get Weather", command=get_weather)
get_button.pack(pady=5)

result_label = Label(root, font=("Arial", 12), justify=LEFT)
result_label.pack(pady=10)

root.mainloop()
