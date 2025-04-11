import os, requests, json
import pyttsx3

def speak_text(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    speak_text("Hello, Welcome to the weather app.")
    
    city = input("Enter the name of your city\n> ")
    
    try:
        url = f"https://api.weatherapi.com/v1/current.json?key=2613a01dd5994ad980b122357251004&q={city}" 
        
        r = requests.get(url)
        wdic = json.loads(r.text)
        
        # Extract weather data
        data1 = (wdic["current"]["temp_c"])
        data2 = (wdic["current"]["condition"]["text"])
        data3 = (wdic["current"]["wind_kph"])
        data4 = (wdic["current"]["humidity"])
        data5 = (wdic["current"]["feelslike_c"]) 
        data6 = (wdic["current"]["vis_km"])
        data7 = (wdic["current"]["gust_kph"])
        
        # Display results in console
        print(f"\nWeather in {city}:")
        print(f"Temperature: {data1}°C")
        print(f"Condition: {data2}")
        print(f"Wind Speed: {data3} km/h")
        print(f"Humidity: {data4}%")
        print(f"Feels Like: {data5}°C")
        print(f"Visibility: {data6} km")
        print(f"Wind Gusts: {data7} km/h\n")
        
        # Comprehensive weather report to speak
        result = (f"The current weather in {city} is {data1} degrees celsius. "
                f"Conditions are {data2}. "
                f"Wind speed is {data3} kilometers per hour. "
                f"Humidity is {data4} percent. "
                f"It feels like {data5} degrees. "
                f"Visibility is {data6} kilometers. "
                f"Wind gusts are up to {data7} kilometers per hour.")
        
        speak_text(result)
        
        # Ask if user wants to check another city
        speak_text("Would you like to check another city's weather?")
        another = input("Would you like to check another city? (yes/no): ").lower()
        
        while another == "yes" or another == "y":
            city = input("\nEnter the name of your city\n> ")
            
            url = f"https://api.weatherapi.com/v1/current.json?key=2613a01dd5994ad980b122357251004&q={city}" 
            
            r = requests.get(url)
            wdic = json.loads(r.text)
            
            data1 = (wdic["current"]["temp_c"])
            data2 = (wdic["current"]["condition"]["text"])
            data3 = (wdic["current"]["wind_kph"])
            data4 = (wdic["current"]["humidity"])
            data5 = (wdic["current"]["feelslike_c"])
            data6 = (wdic["current"]["vis_km"])
            data7 = (wdic["current"]["gust_kph"])
            
            print(f"\nWeather in {city}:")
            print(f"Temperature: {data1}°C")
            print(f"Condition: {data2}")
            print(f"Wind Speed: {data3} km/h")
            print(f"Humidity: {data4}%")
            print(f"Feels Like: {data5}°C")
            print(f"Visibility: {data6} km")
            print(f"Wind Gusts: {data7} km/h\n")
            
            result = (f"The current weather in {city} is {data1} degrees celsius. "
                    f"Conditions are {data2}. "
                    f"Wind speed is {data3} kilometers per hour. "
                    f"Humidity is {data4} percent. "
                    f"It feels like {data5} degrees. "
                    f"Visibility is {data6} kilometers. "
                    f"Wind gusts are up to {data7} kilometers per hour.")
            
            speak_text(result)
            
            speak_text("Would you like to check another city's weather?")
            another = input("Would you like to check another city? (yes/no): ").lower()
        
        speak_text("Thank you for using the weather app. Have a great day!")
        
    except KeyError:
        print("Error: Could not retrieve weather data. Please check the city name and try again.")
        speak_text("Sorry, I couldn't retrieve weather data for that city. Please check the city name and try again.")
    except Exception as e:
        print(f"An error occurred: {e}")
        speak_text("Sorry, an error occurred while processing your request.")