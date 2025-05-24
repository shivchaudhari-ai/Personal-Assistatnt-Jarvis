import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import pyautogui
import requests
import pyjokes
import time

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wish_me():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("I am Jarvis, your personal assistant. How may I help you today?")

def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source, phrase_time_limit=5)
    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that. Could you please repeat?")
        return "None"
    except sr.RequestError:
        speak("Sorry, my speech service is down.")
        return "None"
    return query.lower()

def send_email(to_address, content):
    your_email = "shivam7744998850@gmail.com"
    your_password = "Shivam@161974"
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(your_email, your_password)
        server.sendmail(your_email, to_address, content)
        server.quit()
        speak("Email sent successfully.")
    except Exception as e:
        print(e)
        speak("I couldn't send the email.")

def get_weather(city):
    api_key = "your_openweathermap_api_key"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        response = requests.get(url).json()
        if response["cod"] != "404":
            weather = response["weather"][0]["description"]
            temp = response["main"]["temp"]
            speak(f"The weather in {city} is {weather} with temperature {temp} degrees Celsius.")
        else:
            speak("I couldn't find the weather for that city.")
    except Exception:
        speak("Sorry, I can't get weather info right now.")

def tell_joke():
    joke = pyjokes.get_joke()
    speak(joke)

def main():
    wish_me()
    while True:
        query = take_command()

        if query == "none":
            continue

        elif 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            try:
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except Exception:
                speak("Sorry, I couldn't find anything on Wikipedia.")

        elif 'open youtube' in query:
            speak("Opening YouTube")
            webbrowser.open("https://www.youtube.com")

        elif 'open google' in query:
            speak("Opening Google")
            webbrowser.open("https://www.google.com")

        elif 'open stackoverflow' in query:
            speak("Opening Stack Overflow")
            webbrowser.open("https://stackoverflow.com")

        elif 'the time' in query:
            now = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The time is {now}")

        elif 'open code' in query:
            speak("Opening Visual Studio Code")
            code_path = "C:\\Users\\YourUserName\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            if os.path.exists(code_path):
                os.startfile(code_path)
            else:
                speak("Sorry, I cannot find Visual Studio Code.")

        elif 'send email' in query:
            speak("What should I say?")
            content = take_command()
            speak("Who is the recipient?")
            to = take_command()
            contacts = {
                "shivam": "shivam7744998850@gmail.com",
                "friend": "codewithmilind@gmail.com"
            }
            to_address = contacts.get(to)
            if to_address:
                send_email(to_address, content)
            else:
                speak("I don't have the email address for that contact.")

        elif 'screenshot' in query:
            speak("Taking screenshot")
            image = pyautogui.screenshot()
            image.save("screenshot.png")
            speak("Screenshot saved as screenshot.png")

        elif 'weather' in query:
            speak("Please tell me the city name.")
            city = take_command()
            if city != "none":
                get_weather(city)

        elif 'joke' in query:
            tell_joke()

        elif 'bye' in query or 'exit' in query or 'stop' in query:
            speak("Goodbye! Have a great day.")
            break

        else:
            speak("Sorry, I don't understand that command. Please try again or ask for help.")

if __name__ == "__main__":
    main()
