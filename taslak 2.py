texty="Click on help to listen the guide"
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

root = Tk()
root.title("BINANI ASSITANT")
root.iconbitmap=('Untitled-5.ico')

#the email data

def city(city):
    global api_address
    api_address = 'http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=bbfb606399d3c2466201a62bdbbba5ec'




class color:
    pURPLE = '\033[95m'
    cYAN = '\033[96m'
    dARKCYAN = '\033[36m'
    bLUE = '\033[94m'
    bREEN = '\033[92m'
    yELLOW = '\033[93m'
    rED = '\033[91m'
    bOLD = '\033[1m'
    uNDERLINE = '\033[4m'
    eND = '\033[0m'
    rEDD = '\033[0;37;44m'
    bLUE = '\033[0;34;48m'
    rED = '\033[0;31;48m'



# CALC .GET DEF,FUNCTION
def get_operator_fn(op):
    return {
        '+': operator.add,
        '-': operator.sub,
        'by': operator.mul,
        'divided': operator.__truediv__,
        '/': operator.__truediv__,
        'Mod': operator.mod,
        'mod': operator.mod,
        '^': operator.xor,
    }[op]


def eval_binary_expr(op1, oper, op2):
    op1, op2 = int(op1), int(op2)
    return get_operator_fn(oper)(op1, op2)



def talkToMe(audio):
    "voice to text"

    sayer = pyttsx3.init()
    sayer.say(audio)
    sayer.setProperty('rate', 100)
    sayer.runAndWait()

    #  use the system's inbuilt say command instead of mpg123
    #  text_to_speech = gTTS(text=audio, lang='en')
    #  text_to_speech.save('audio.mp3')
    #  os.system('mpg123 audio.mp3')

talkToMe("click on help to listen the guide")

MyEntry = Entry(root, width=60, borderwidth=5)
MyEntry.insert(0, "")
MyEntry.pack()

def notPrint(idkwhat):
    e = MyEntry
    e.delete(0, END)
    e.insert(0, idkwhat)
notPrint("Click on help to listen the guide")
def myCommand():
    "listens for commands"

    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:

        command = r.recognize_google(audio).lower()
        notPrint('You said: ' + command + '\n')


    #loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:
        notPrint('Your last command couldn\'t be heard')


    return command



def assistant(command):
    "if statements for executing commands"

    if 'open reddit' in command:
        reg_ex = re.search('open reddit (.*)', command)
        url = 'https://www.reddit.com/'
        if reg_ex:
            subreddit = reg_ex.group(1)
            url = url + 'r/' + subreddit
        webbrowser.open(url)


    elif "calculate" in command:
        reg_ex = re.search('calculate (.*)', command)
        if reg_ex:
            firststring = reg_ex.group(1)

        stringfinal = eval_binary_expr(*(firststring.split()))
        say_final_calculator = str(firststring) + " is EQUAL TO " + str(stringfinal)
        notPrint(say_final_calculator)
        talkToMe(say_final_calculator)


    elif "link" in command:


        talkToMe("I will shrink the link you have copied and i will copy it for you")
        link = clip.paste()
        notPrint(shortener.Shortener().clckru.short(link))
        clip.copy(shortener.Shortener().clckru.short(link))
        time.sleep(1)


    elif 'open website' in command:
        reg_ex = re.search('open website (.+)', command)
        if reg_ex:
            domain = reg_ex.group(1)
            url = 'https://www.' + domain +'.com'
            webbrowser.open(url)
            notPrint("DONE! :) ")
        else:
            pass

    elif 'what\'s up' in command:
        talkToMe('Just doing my thing')
    elif 'joke' in command:
        res = requests.get(
                'https://icanhazdadjoke.com/',
                headers={"Accept":"application/json"}
                )
        if res.status_code == requests.codes.ok:
            talkToMe(str(res.json()['joke']))
        else:
            talkToMe('oops!I ran out of jokes')

    elif 'how is the weather in' in command:
        reg_ex = re.search('how is the weather in (.*)', command)
        if reg_ex:
            city = reg_ex.group(1)
            #weather = Weather()
            #location = weather.lookup_by_location(city)
            #condition = location.condition()
            #talkToMe('The Current weather in %s is %s The tempeture is %.1f degree' % (city, condition.text(), (int(condition.temp())-32)/1.8))
            data = YahooWeather(APP_ID="BLQDcnV3",
                                api_key="dj0yJmk9SVUySXpDUFZLbW9yJmQ9WVdrOVFreFJSR051VmpNbWNHbzlNQT09JnM9Y29uc3VtZXJzZWNyZXQmc3Y9MCZ4PWU2",
                                api_secret="2634a951ac818fc459c21ce072d7a4014c3a4a2a")
            stringCity = str(city)
            data.get_yahoo_weather_by_city(city, Unit.celsius)
            notPrint(f'the tempreature in {stringCity} is {data.condition.temperature} and the weather condition is {data.condition.text}')
            talkToMe(f'the tempreature in {stringCity} is {data.condition.temperature} and the weather condition is {data.condition.text}')

    elif 'email' in command:
       try:
           text = open("mailPassAndUsername.txt")
           emailandusername = []
           for line in text:
               emailandusername.append(line.strip())

           text.close()
           print(emailandusername)
           sender_email = emailandusername[0]
           password = emailandusername[1]
           reciever = emailandusername[2]
           outputmessage = ""
           message = emailandusername[3:]

           finalMessage = ' '.join(map(str, message))

           server = smtplib.SMTP('smtp.gmail.com', 587)  # Connect to the server
           server.starttls()  # Use TLS
           server.login(sender_email, password)  # Login to the email server
           server.sendmail(sender_email, reciever, finalMessage)  # Send the email
           server.quit()  # Logout of the email server
           print("done")

           print(finalMessage)



       except:
            talkToMe("Im not siri sir be more specific lets take it again")
            myCommand()


#talkToMe('I am ready for your command')

#loop to continue executing multiple commands
#while True:
    #assistant(myCommand())
def button_main():
    assistant(myCommand())


talkImage1 = PhotoImage(file='title--1.png')
Button(root,text="Help",command=lambda : talkToMe("I cand calculate you tell me ten by eleven i tell you the result you tell me shrink the link i have copied i do you tellme open website youtube i do actully you can tell me to open any website i can send emails too but thats a little bit advanced but i can i can tell you the weather in a specific city as an example  say how is the weather in istanbul  ican do more and more like i can tell you jokes!")).pack()
Button(root,image=talkImage1,pady=20,padx=5,command=button_main,borderwidth=0).pack(pady=20)
mainloop()

