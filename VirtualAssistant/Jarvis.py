from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import os
import time
import pyttsx3
import speech_recognition as sr
import pytz
import subprocess
import playsound
import random
import webbrowser
import sys

SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
MONTHS = ["january", "february", "march", "april", "may", "june","july", "august", "september", "october", "november", "december"]
DAYS = ["monday", "tuesday", "wednesday","thursday", "friday", "saturday", "sunday"]
DAY_EXTENTIONS = ["rd", "th", "st", "nd"]

# Commands

PHRASES__FOR_COMMANDS = ["sure", "right away", "sure thing"]
PHRASES__FOR_WAITING = ["let me check","just a moment", "hang on a moment"]
PHRASES__FOR_COMPLETION = ["and done", "here you go","and you are set"]
SLEEP_STRINGS = ["good night", "go to sleep", "sleep","we will see later", "we will talk later", "take some rest"]
NOTE_STRINGS = ["make a note", "note this down", "note this", "remember this"]
CALENDAR_STRINGS = ["what do i have", "do i have plans","am i busy", " what's on", "any plans"]
CP_PHRASES = ["setup", "competitive coding"]

# Basic Input/Output stuff

def speak(text):
   
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source,phrase_time_limit=5)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception: " + str(e))
    return said.lower()

# Accessing Google Calendar

def authenicate_google_calendar():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)

    return service

# Google Calendar stuff

def get_events(day, service):
    # Call the Calendar API
    date = datetime.datetime.combine(day, datetime.datetime.min.time())
    end_date = datetime.datetime.combine(day, datetime.datetime.max.time())
    utc = pytz.UTC
    date = date.astimezone(utc)
    end_date = end_date.astimezone(utc)

    events_result = service.events().list(calendarId='primary', timeMin=date.isoformat(), timeMax=end_date.isoformat(),
                                          singleEvents=True,
                                          orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        speak('No upcoming events found. i guess you are free for the day.')
    else:
        speak(f"you have {len(events)} events on this day.")
        
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            print(start, event['summary'])
            start_time = str(start.split("T")[1].split("+")[0])
            if int(start_time.split(":")[0]) < 12:
                if start_time.split(":")[1] == "00":
                    start_time = str(int(start_time.split(":")[0]))
                else:
                    start_time = str(int(start_time.split(
                        ":")[0])) + " " + start_time.split(":")[1]
                start_time += " A M"
            else:
                if start_time.split(":")[1] == "00":
                    start_time = str(int(start_time.split(":")[0])-12)
                else:
                    start_time = str(int(start_time.split(
                        ":")[0])-12) + " " + start_time.split(":")[1]
                start_time += " P M"

            speak(event["summary"] + " at " + start_time)

def get_date(text):
    text = text.lower()
    today = datetime.date.today()

    if text.count("today") > 0:
        return today

    day = -1
    day_of_week = -1
    month = -1
    year = today.year

    for word in text.split():
        if word in MONTHS:
            month = MONTHS.index(word)+1

        elif word in DAYS:
            day_of_week = DAYS.index(word)
        elif word.isdigit():
            day = int(word)
        else:
            for ext in DAY_EXTENTIONS:
                found = word.find(ext)
                if found > 0:
                    try:
                        day = int(word[:found])

                    except:
                        pass

    if month < today.month and month != -1:
        year += 1

    if day < today.day and month == -1 and day != -1:
        month += 1

    if month == -1 and day == -1 and day_of_week != -1:
        current_day_of_week = today.weekday()
        dif = day_of_week - current_day_of_week

        if dif < 0:
            dif += 7
            if text.count("next") >= 1:
                dif += 7

        return today + datetime.timedelta(dif)

    tomorrow = datetime.date.today() + datetime.timedelta(days=1)
    if text.count("tomorrow") > 0:
        return tomorrow

    if month == -1 or day == -1:
        return None
    return datetime.date(month=month, day=day, year=year)

def note(text):
    date = datetime.datetime.now()
    file_name = "Path\\To\\Required\\Folder" + \
        str(date).replace(":", "-") + "-note.txt"

    with open(file_name, "w") as f:
        f.write(text)

    x = subprocess.Popen(["notepad.exe", file_name])
    x.terminate()
    

# Wake

Name = "jarvis"
service = authenicate_google_calendar()
speak("Hi i am %s. your virtual assistant" % Name)
print("Start")

while True:
    print("Listening")

    text = get_audio()

    if text.count(Name) > 0:
        speak("i am listening")
        text = get_audio()

        # Calendar 
              
        for phrase in CALENDAR_STRINGS:
            if phrase in text:
                date = get_date(text)
                if date:
                    i = random.choice(
                        range(0, len(PHRASES__FOR_WAITING)))
                    speak(PHRASES__FOR_WAITING[i])
                    get_events(date, service)
                else:
                    speak("i don't understand")
       
        # Notes 
               
        for phrase in NOTE_STRINGS:
            if phrase in text:
                i = random.choice(range(0, len(PHRASES__FOR_COMMANDS)))
                speak(PHRASES__FOR_COMMANDS[i])
                speak("what would you like me to write down?")
                note_text = get_audio()
                note(note_text)
                speak("I have made a note of that")

        # Opening apps,files

        if "open" in text:

            # Open VS Code
            if "vs code" in text:
                i = random.choice(range(0, len(PHRASES__FOR_WAITING)))
                speak(PHRASES__FOR_WAITING[i])
                os.system("code")                
                i = random.choice(range(0, len(PHRASES__FOR_WAITING)))
                speak(PHRASES__FOR_COMPLETION[i])

            # Open College materials folder
            if "college materials" in text:
                i = random.choice(range(0, len(PHRASES__FOR_WAITING)))
                speak(PHRASES__FOR_WAITING[i])
                os.startfile("Censored\\college related")
                i = random.choice(range(0, len(PHRASES__FOR_WAITING)))
                speak(PHRASES__FOR_COMPLETION[i])

            if "competitive coding book" in text:
                i = random.choice(range(0, len(PHRASES__FOR_WAITING)))
                speak(PHRASES__FOR_WAITING[i])
                os.startfile("Censored\\Competitive Coding\\Competitive programming.pdf")
                i = random.choice(range(0, len(PHRASES__FOR_WAITING)))
                speak(PHRASES__FOR_COMPLETION[i])
        
        # CP setup

        for phrase in CP_PHRASES:
            if phrase in text:
                speak("which website?")
                text = get_audio()
                if "chef" in text:
                    i = random.choice(
                        range(0, len(PHRASES__FOR_WAITING)))
                    speak(PHRASES__FOR_WAITING[i])
                    os.startfile(
                        "Censored\\Codechef\\Codechef CP.sublime-workspace")
                    webbrowser.open("https://www.codechef.com/")
                    i = random.choice(
                        range(0, len(PHRASES__FOR_WAITING)))
                    speak(PHRASES__FOR_COMPLETION[i])

                if "forces" in text:
                    i = random.choice(
                        range(0, len(PHRASES__FOR_WAITING)))
                    speak(PHRASES__FOR_WAITING[i])
                    os.startfile(
                        r"Censored\Codeforces\Codeforces CP.sublime-workspace")
                    webbrowser.open("https://codeforces.com/problemset?order=BY_RATING_ASC")
                    i = random.choice(
                        range(0, len(PHRASES__FOR_WAITING)))
                    speak(PHRASES__FOR_COMPLETION[i])
        
        # Sleep

        for phrase in SLEEP_STRINGS:
            if phrase in text:
                speak("Good night")
                exit()
