import pyttsx3
import speech_recognition as sr
import pyaudio
import os
import pywhatkit as kit
import sqlite3
import webbrowser
import features_VA.helper as hlp
import eel

global speak
speak = pyttsx3.init()

global understand
understand = sr.Recognizer()
a = 0

con = sqlite3.connect("Voice_Assistant.db")
cursor = con.cursor()

def intro_speak(query):
    e = speak
    e.say(query)
    e.runAndWait()

def speaking(query):
    from features_VA.CONSTANT import Voice_Number
    voices = speak.getProperty("voices")
    speak.setProperty("voice",voices[Voice_Number].id)
    speak.say(query)
    speak.runAndWait()
    eel.ShowHood()

def listening():
    with sr.Microphone() as source:
        print("Listnening....")
        eel.Displaymsg("listening....")
        understand.pause_threshold = 0.8
        understand.adjust_for_ambient_noise(source)

        audio = understand.listen(source,10,6)
    
    return audio

def query_creation():
    audio = listening()
    try:
        print("Understanding....")
        eel.Displaymsg("Understanding....")
        query = understand.recognize_google(audio,language="en-in")
        eel.Displaymsg(query)
        return query
    except:
        print("Unable to Understand")
        speaking("Unable to Understand")
        return None


def opencom(query):
    query = query.replace("open","")
    query = query.lower()
    print(query)
    app_name = query.strip()
    print(app_name)
    if app_name != "":
        try:
            cursor.execute("SELECT path FROM sys_command WHERE name IN (?)",(app_name,))
            result = cursor.fetchall()

            if len(result) != 0:
                speaking("Opening "+app_name)
                os.startfile(result[0][0])

            elif len(result) == 0:
                cursor.execute("SELECT url FROM web_command WHERE name IN (?)",(app_name,))
                result = cursor.fetchall()

                if len(result) != 0:
                    speaking("Opening "+app_name)
                    webbrowser.open(result[0][0])
                
                else:
                    speaking("Opening "+app_name)
                    try:
                        os.system("start "+app_name)
                    except:
                        speaking("Not Found")
        except:
            speaking("Something Went Wrong")
    else:
        speaking("Error")

def PlayYoutube(query):
    search_term = hlp.extract_yt_term(query)
    a = f"Playing {query} on Youtube"
    speaking(a)
    kit.playonyt(search_term)

def search_query(query):
    if "search" in query:
        query = query.replace("search","")
    else:
        query = query.replace("search this","")
    query = query.strip()
    query = query.replace(" ","+")
    url = f'https://google.com/search?q={query}'
    webbrowser.open(url)