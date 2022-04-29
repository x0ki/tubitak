from gtts import gTTS
from playsound import  playsound
from gtts import gTTS
import speech_recognition as sr
import os
import re
from yahoo_weather.weather import YahooWeather
from yahoo_weather.config.units import Unit
import webbrowser
import smtplib
import requests
#from weather import Weather
from playsound import  playsound
import operator
import time
import pywhatkit as kit
import pyperclip as clip
import pyshorteners as shortener
import pyttsx3
from tkinter import *
import random
import gtts


def sayer(mytext):
    language='tr'
    voicefile=gTTS(text=mytext,lang=language,slow=False)
    voicefile.save("ses.mp3")
    playsound("ses.mp3")
    os.remove('ses.mp3')

sayer('dinliyorum dostum')

def myCommand():
    "listens for commands"

    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:

        command = r.recognize_google(audio , language='tr-TR').lower()


    #loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:
        sayer('bir daha söyle bakim')
        myCommand()
    return command



while True:
    emir=myCommand()

    if 'nasılsın' in emir:
        print('dinledim')
        sayer('bu seni hiç alakadar etmez')
    elif 'adın' or 'ismin' in emir:
        sayer('benim adım ezel ve buraya intikam almaya geldim')
    elif 'ezel senmisin':
        sayer('bu karizma başka kimin olabilirki')
    else:
        pass





