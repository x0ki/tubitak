
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

#if __name__ == '__main__':
 #   board = pyfirmata.Arduino('COM4')
  #  print("Communication Successfully started")


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
    sayer.say(audio)
    sayer.runAndWait()

    #  use the system's inbuilt say command instead of mpg123
    #  text_to_speech = gTTS(text=audio, lang='en')
    #  text_to_speech.save('audio.mp3')
    #  os.system('mpg123 audio.mp3')

talkToMe("say help to liste the guide")
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

    elif 'light' and "on" in command:
        board.digital[8].write(1)

    elif "light" and "off" in command:
        board.digital[8].write(0)



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

    elif 'how is the weather in' in command:
        reg_ex = re.search('how is the weather in (.*)', command)
        if reg_ex:
            city = reg_ex.group(1)
            weather = Weather()
            location = weather.lookup_by_location(city)
            condition = location.condition()
            talkToMe('The Current weather in %s is %s The tempeture is %.1f degree' % (city, condition.text(), (int(condition.temp())-32)/1.8))

    elif 'weather forecast in' in command:
        reg_ex = re.search('weather forecast in (.*)', command)
        if reg_ex:
            city = reg_ex.group(1)
            weather = Weather()
            location = weather.lookup_by_location(city)
            forecasts = location.forecast()
            for i in range(0,3):
                talkToMe('On %s will it %s. The maximum temperture will be %.1f degree.'
                         'The lowest temperature will be %.1f degrees.' % (forecasts[i].date(), forecasts[i].text(), (int(forecasts[i].high())-32)/1.8, (int(forecasts[i].low())-32)/1.8))


    elif 'email' or 'mail' in command:
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


talkToMe('I am ready for your command')

#loop to continue executing multiple commands
while True:
    assistant(myCommand())