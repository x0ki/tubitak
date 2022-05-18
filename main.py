from gtts import gTTS
import pyfirmata
import speech_recognition as sr
import os
import re
import webbrowser
import smtplib , ssl
import requests
#from weather import Weather
import operator
import time
#import pywhatkit as kit
import pyperclip as clip
import pyshorteners as shortener
import pyttsx3
import random

VARbed = 0
VARdine = 0
VARlive = 0

aONLIST = ['i cant turn the same thing on while it is already on' , 'it is already on sir','i guess u are blind, sorry bad news']
aOFFLIST = ['can you turn the same thing off twice? no you cant , so cant i', 'already off']



if __name__ == '__main__':
    board = pyfirmata.Arduino('COM5')
    print("Communication Successfully started")


offList = ['in case you want it off , just let me know' , 'dont forget to inform once you want it off' , 'i would love to help you again if you want to turn it off again' , 
'done' , 'blink! , it is off']

onList = ['you got my light , didnt you?' , 'do i have to do all the work my self?' , 'you must thank allah that the developer made me']

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


def calclulator(command):
    reg_ex = re.search('calculate (.*)', command)
    if reg_ex:
        firststring = reg_ex.group(1)

    talkToMe("What do you want to calculate? As an example eight plus ten")
    stringfinal = eval_binary_expr(*(firststring.split()))
    print(color.bLUE + str(firststring) + color.eND + color.rED + " IS EQUAL TO " + color.eND + color.rED + str(
        stringfinal) + color.eND)
    say_final_calculator = str(text) + " is EQUAL TO " + str(stringfinal)
    talkToMe(say_final_calculator)

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
    "speaks audio passed as argument"

    sayer = pyttsx3.init()
    sayer.setProperty('rate',140)
    sayer.say(audio)
    sayer.runAndWait()

    #  use the system's inbuilt say command instead of mpg123
    #  text_to_speech = gTTS(text=audio, lang='en')
    #  text_to_speech.save('audio.mp3')
    #  os.system('mpg123 audio.mp3')

talkToMe("say help to listen the guide")
def myCommand():
    "listens for commands"

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Ready...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio).lower()
        print('You said: ' + command + '\n')

    #loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:
        print('Your last command couldn\'t be heard')
        command = myCommand();

    return command


def assistant(command):
    "if statements for executing commands"
    #more developed lightning variables
    global VARbed 
    global VARdine 
    global VARlive 


    if 'open reddit' in command:
        reg_ex = re.search('open reddit (.*)', command)
        url = 'https://www.reddit.com/'
        if reg_ex:
            subreddit = reg_ex.group(1)
            url = url + 'r/' + subreddit
        webbrowser.open(url)
        print('Done!')

    elif "calculate" in command:
        reg_ex = re.search('calculate (.*)', command)
        if reg_ex:
            firststring = reg_ex.group(1)

        stringfinal = eval_binary_expr(*(firststring.split()))
        print(color.bLUE + str(firststring) + color.eND + color.rED + " IS EQUAL TO " + color.eND + color.rED + str(
            stringfinal) + color.eND)
        say_final_calculator = str(firststring) + " is EQUAL TO " + str(stringfinal)
        talkToMe(say_final_calculator)


    elif "link" in command:

        print(color.bLUE + """
    I will short the link you have copied and i will
    print and copy the shortened link :)
        """ + color.eND)
        talkToMe("I will shrink the link you have copied and i will copy it for you")
        link = clip.paste()
        print(shortener.Shortener().clckru.short(link))
        clip.copy(shortener.Shortener().clckru.short(link))

        print(color.rED + """DONE :)""" + color.eND)
##-------------------------------------------------------------------#
    elif 'living' in command:
        
        if 'on' in command:
            if VARlive == 0:
                board.digital[3].write(1)
                talkToMe( random.choice(onList) )
                VARlive = 1
            else:
                talkToMe(random.choice(aONLIST))
            
        elif 'off' in command:
            if VARlive == 1:
                board.digital[3].write(0)
                talkToMe( random.choice(offList) )
                VARlive = 0
            else:
                talkToMe(random.choice(aOFFLIST))  

    
    elif 'bedroom' in command:
        if 'on' in command:
            if VARbed == 0:
                board.digital[2].write(1)
                talkToMe( random.choice(onList) )
                VARbed = 1
            else:
                 talkToMe(random.choice(aONLIST))

        elif 'off' in command:
            if VARbed == 1:
                board.digital[2].write(0)
                talkToMe( random.choice(offList) )
                VARbed = 0
            else:
                talkToMe(random.choice(aOFFLIST))

    

    elif 'email' in command:
        talkToMe('Who is the recipient?')
        recipient = myCommand()

        if 'Alex' or 'alex' in recipient:
            port = 587  # For starttls
            smtp_server = "smtp.gmail.com"
            sender_email = "ezelarap24@gmail.com"
            receiver_email = "ezel@bayraktar.ltd"
            password = "Bnan@2003"
            talkToMe('what shall i tell')
            message = myCommand()

            context = ssl.create_default_context()
            with smtplib.SMTP(smtp_server, port) as server:
                server.ehlo()  # Can be omitted
                server.starttls(context=context)
                server.ehlo()  # Can be omitted
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, message)
            talkToMe('Email sent.')

        else:
            talkToMe('I don\'t know what you mean!')



    elif 'dining' in command:
        if 'on' in command:
            if  VARdine==0:
                board.digital[4].write(1)
                VARdine = 1
                talkToMe( random.choice(onList) )
                
            else:
                talkToMe(random.choice(aONLIST))

        elif 'off' in command:
            if VARdine == 1:
                board.digital[4].write(0)
                talkToMe( random.choice(offList) )
                VARdine = 0
            else:
                talkToMe(random.choice(aOFFLIST))

##----------------------------------------------------##
    elif 'open website' in command:
        reg_ex = re.search('open website (.+)', command)
        if reg_ex:
            domain = reg_ex.group(1)
            url = 'https://www.' + domain +'.com'
            webbrowser.open(url)
            print('Done!')
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

    elif 'weather in ' in command:
        city1 = command.split()
        city = city1[-1]
        BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
        CITY = city
        API_KEY = "c03763c5734acd536e1c4a5bde1e5df8"

        URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY

        response = requests.get(URL)

        if response.status_code == 200:
            data = response.json()
            main = data['main']
            temperature = main['temp']
            humidity = main['humidity']
            pressure = main['pressure']
            report = data['weather']
            print(f"{CITY:-^30}")
            print(f"Temperature: {temperature}")
            print(f"Weather Report: {report[0]['description']}")
            rep0rt=report[0]['description']
            tC=int(temperature)-273
            talkToMe(f'the current weather in {city} is {rep0rt} and the temprature is {tC}')
        else:
            print("Error in the HTTP request")
            talkToMe('i got an issue')
    else:
        talkToMe(random.choice('what','sorry i didnt get it , may you repeat'))



    


talkToMe('I am ready for your command')

#loop to continue executing multiple commands
while True:
    assistant(myCommand())