import datetime
import re
import smtplib
import threading
import time
import json
import pyttsx3
import speech_recognition as sr
import os
import wikipedia as wikipedia
import webbrowser
import random
import requests
import pyjokes
from Speak import engine
from twilio.rest import Client


print("Initializing G16 Voice assistant...........")
#dict = {'Narendra': 'narendrasencha@gmail.com', 'Akku': 'narendrasencha201@gmail.com'}
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

account_sid = "ACc33393ac940eca481c3d1b7e18046b59"
auth_token = "a33a9228ecade56efd2997559c9d9d0e"


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def WishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir !!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon sir!!")
    else:
        speak("Good Evening sir!!")

    speak("Hi, This is G16 voice assistant. How may i help you")
    #print("Hi, This is G16 voice assistant. How may i help you")




def TakeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nListening...")
        #speak("Listening....")
        audio = r.listen(source, phrase_time_limit=5)
        try:
            print("Recognizing...")
            #speak("Recognizing....")
            query = r.recognize_google(audio, language='en-in')  # Using google for voice recognition.
            print(f"User said: {query}\n")  # User query will be printed.

        except Exception as e:
            speak("say that again please...")
            print("Say that again please...")  # Say that again will be printed in case of improper voice
            return "None"  # None string will be returned
        return query

def saveReminder(content):
    if "remind me to" in content:

        content = content.replace("remind me to","")
        Reminder = open(r"Reminders.txt", "a+")
        Reminder.write(content)
        Reminder.close()

    #To get reminders
def getReminders():
    Reminder = open(r"Reminders.txt", "r+")
    speak(Reminder.readlines)
    Reminder.close()

def sendEmail(to, content):

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("narendrasencha2000@gmail.com", "Jaygurudev@2480")
    server.sendmail("narendrasencha2000@gmail.com", to, content)
    server.close()


def Mainclass():
    talk = ""
    speak("Initializing G16 Voice assistant...........")
    WishMe()
    while True:
        query = TakeCommand()
        talk = query

        if "who are you" in query.lower() or "introduce yourself" in query.lower():
            speak("My name is G16. I am an Artificial Intelligence Assistant program.")

        elif 'wikipedia' in query.lower():
            speak("Searching wikipedia....")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            print(results)
            speak(results)

        elif 'open youtube' in query.lower():
            webbrowser.register('chrome', None,
                                webbrowser.BackgroundBrowser("C:\Program Files\Google\Chrome\Application\chrome.exe"))
            url = "youtube.com"
            print("Opening Youtube...")
            speak("Opening youtube")
            webbrowser.get('chrome').open_new(url)

        elif 'open google' in query.lower():
            webbrowser.register('chrome', None,
                                webbrowser.BackgroundBrowser("C:\Program Files\Google\Chrome\Application\chrome.exe"))
            url = "google.com"
            print("Opening google...")
            speak("Opening google")
            webbrowser.get('chrome').open_new(url)

        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")

        elif 'open stack' in query.lower():
            webbrowser.register('chrome', None,
                                webbrowser.BackgroundBrowser("C:\Program Files\Google\Chrome\Application\chrome.exe"))
            url = "stackoverflow.com"
            print("Opening stackoverflow...")
            speak("Opening stackoverflow")
            webbrowser.get('chrome').open_new(url)

        elif 'open reddit' in query.lower():
            webbrowser.register('chrome', None,
                                webbrowser.BackgroundBrowser("C:\Program Files\Google\Chrome\Application\chrome.exe"))
            url = "reddit.com"
            print("Opening reddit...")
            speak("Opening reddit")
            webbrowser.get('chrome').open_new(url)

        elif 'open github' in query.lower():
            webbrowser.register('chrome', None,
                                webbrowser.BackgroundBrowser("C:\Program Files\Google\Chrome\Application\chrome.exe"))
            url = "github.com"
            print("Opening github...")
            speak("Opening github")
            webbrowser.get('chrome').open_new(url)

        elif 'open linkedin' in query.lower():
            webbrowser.register('chrome', None,
                                webbrowser.BackgroundBrowser("C:\Program Files\Google\Chrome\Application\chrome.exe"))
            url = "https://in.linkedin.com"
            print("Opening Linkedin...")
            speak("Opening Linkedin")
            webbrowser.get('chrome').open_new(url)


        elif 'play music' in query.lower():
            songs_dir = "C:\\Users\\naren\\Music"
            songs = os.listdir(songs_dir)
            print(songs)
            d = random.choice(songs)
            os.startfile(os.path.join(songs_dir, d))

        elif 'the time' in query.lower():
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"The time is :{strTime}")
            speak(f"The time is :{strTime}")

        elif 'open anaconda' in query.lower():  # error opening in anaconda
            path_ana = "C:\\Users\\naren\\anaconda3\\pythonw.exe C:\\Users\\naren\\anaconda3\\cwp.py " \
                       "C:\\Users\\naren\\anaconda3 C:\\Users\\naren\\anaconda3\\pythonw.exe " \
                       "C:\\Users\\naren\\anaconda3\\Scripts\\spyder-script.py "
            print("Opening anaconda")
            speak("Opening anaconda")
            os.startfile(os.path.join(path_ana))

        elif 'email' in query.lower():
            try:
                speak("To whom email to be send")
                print("To whom email to be send")
                to_temp = TakeCommand()
                dict = {'Narendra': 'narendrasencha@gmail.com', 'Akku': 'narendrasencha201@gmail.com','Rajesh':'rajeshkchakrawarti@svvv.edu.in'}
                to = dict.get(to_temp)
                if (not to):
                    print("Email for this user not found")
                    speak("Email for this user not found ")

                else:
                    speak("What should I send")
                    print("What should i send")
                    content = TakeCommand()
                    sendEmail(to, content)
                    speak("Email has been sent successfully")
                    print("Email has been sent successfully")

            except Exception as e:
                print(e)

        elif "set a reminder" in query.lower():
            try:
                speak("What should I remind you ?")
                content = TakeCommand()
                saveReminder(content)
                speak("Reminder saved")
            except Exception as e:
                speak("Sorry could not set reminder")

        elif "my reminders" in query.lower():
            try:
                getReminders()
                speak("I guess that's all I had to remind you, bro")
            except Exception as e:
                speak("Sorry could not fetch reminders")

        elif "toss a coin" in query.lower():
            coinResult = random.randint(0, 1)
            if coinResult == 0:
                speak("Its a Head!")
            else:
                speak("Its Tails!")

        elif 'joke' in query.lower():
            speak(pyjokes.get_joke())

        elif 'weather' in query.lower():
            api_key = "8ef61edcf1c576d65d836254e11ea420"
            base_url = "https://api.openweathermap.org/data/2.5/weather?"
            speak("whats the city name")
            city_name = TakeCommand()
            complete_url = base_url + "appid=" + api_key + "&q=" + city_name
            response = requests.get(complete_url)
            x = response.json()
            if x["cod"] != "404":

                y = x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))

            else:
                speak(" City Not Found ")


        elif "send message" in query:

            # You need to create an account on Twilio to use this service
            #account_sid = UserCreds.account_sid
            #auth_token = UserCreds.auth_token
            client = Client(account_sid, auth_token)
            speak("What should I say?")
            content = TakeCommand()

            # adding twilio number to verified number from UserCreds.py
            try:
               message = client.messages \
                    .create(
                            body=content,
                            from_='+18505429408',
                            to='+919589805187'
                    )
               speak("SMS send successfully")
            except Exception as e:
                print(e)
                speak("Sorry was not able to send message.")


        elif 'goodbye' in query.lower():
            speak("Shutting down G16 voice assistant")
            speak("Thank you for using G16 Voice assistant")
            exit()


