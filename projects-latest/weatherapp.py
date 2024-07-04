import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import requests

def get_weather():
    city = city_entry.get()
    api_key = "390ace727ff6fe3aec1108666bb9a8c2"
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    complete_url = f"{base_url}?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(complete_url)
        weather_data = response.json()

        if weather_data["cod"]!= "404":
            main = weather_data["main"]
            temperature = main["temp"]
            pressure = main["pressure"]
            humidity = main["humidity"]
            weather_desc = weather_data["weather"][0]["description"]

            weather_info = (
                f"Temperature: {temperature}°C\n"
                f"Pressure: {pressure} hPa\n"
                f"Humidity: {humidity}%\n"
                f"Description: {weather_desc}"
            )

            # Update weather information label with larger font
            weather_label.config(text=weather_info, font=("Arial", 18))

            # Update weather image
            if "sunny" in weather_desc.lower():
                img_path = "sunny.png"
                background_img_path = "sunny.png"
            elif "cloud" in weather_desc.lower():
                img_path = "sunny.png"
                background_img_path = "sunny.png"
            elif "rain" in weather_desc.lower():
                img_path = "sunny.png"
                background_img_path = "sunny.png"
            else:
                img_path = "sunny.png"
                background_img_path = "sunny.png"

            try:
                # Update background image
                background_img = Image.open(background_img_path)
                background_img = background_img.resize((800, 600), Image.LANCZOS)  # Adjust size as needed
                background_img = ImageTk.PhotoImage(background_img)
                background_label.config(image=background_img)
                background_label.image = background_img
            except Exception as e:
                print(f"Error loading image: {e}")
                weather_image_label.config(image=None)
                background_label.config(image=None)

        else:
            weather_label.config(text="City Not Found", font=("Arial", 18))
            weather_image_label.config(image=None)
            background_label.config(image=None)
    except Exception as e:
        print(f"Error occurred: {e}")
        messagebox.showerror("Error",
                             "Unable to get weather data. Please check your internet connection and try again.")

root = tk.Tk()
root.title("Weather Application")
root.geometry("800x600")  # Adjusted window size to be larger
root.resizable(False,False)
root.configure(background="#f0f0f0")  # Light gray background

# Load default background image
default_background_img = Image.open("default.png")
default_background_img = default_background_img.resize((800, 600), Image.LANCZOS)  # Adjust size as needed
default_background_img = ImageTk.PhotoImage(default_background_img)
background_label = tk.Label(root, image=default_background_img)
background_label.place(x=0, y=0)

# Create a frame for the input fields
mytitle = tk.Label(root, text="WEATHER APP", font=("Arial", 30, "bold"), bg="#008080", fg="white")
mytitle.pack(side=tk.TOP, fill='x', pady=40)

input_frame = tk.Frame(root, bg="#f0f0f0", bd=2, relief=tk.SOLID)
input_frame.pack(pady=20)

city_label = tk.Label(input_frame, text="Enter City:", font=("Arial", 18), bg="#f0f0f0")
city_label.pack(side=tk.LEFT, padx=10)

city_entry = tk.Entry(input_frame, width=25, font=("Arial", 18))
city_entry.pack(side=tk.LEFT, padx=10)

get_weather_button = tk.Button(input_frame, text="Get Weather", font=("Arial", 18), bg="#4CAF50", fg="white",
                               command=get_weather)
get_weather_button.pack(side=tk.LEFT, padx=10)

# Create a frame for the weather information
weather_frame = tk.Frame(root, bg="#f0f0f0", bd=2, relief=tk.SOLID)
weather_frame.pack(pady=40)

weather_label = tk.Label(weather_frame, text="", font=("Arial", 18), bg="#f0f0f0", wraplength=700)
weather_label.pack(pady=10)

weather_image_label = tk.Label(weather_frame, image=None, bg="#f0f0f0")
weather_image_label.pack(pady=10)

root.mainloop()