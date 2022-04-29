import operator
import speech_recognition as sr
import webbrowser
import time
import pywhatkit as kit
import pyperclip as clip
import pyshorteners as shortener
import pyttsx3

def recagnition(x):
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        try:
            x = r.recognize_google(audio)
        except:
            print(color.rED + "Sorry?" + color.eND)
    return x

search = ""
youtubee = ""
text = ""
choice = ""

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



sr.Microphone(device_index=1)
r = sr.Recognizer()


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





print(color.bLUE + """
 Hey sir its Binan!
Iam using google voice recognition!
Which service you want to use?
1 - VOICE ASSISTED WEB SEARCH
2 - VOICE ASSISTED CALCULATOR
3 - VOICE ASSISTED YOUTUBE SEARCH
4 - LINK SHORTNER

Ex:- Choose VOICE ASSISTED WEB SEARCH
MORE ASAP...
""" + color.eND)


intro = pyttsx3.init()
intro.say("Hey sir its the big b i am using google voice recognition. which service do you want to use? i have a voice assisted web search voice assisted calculator i also have a link shortener and last but not least the voice assisted youtube search to choose one of my services just say its name")
intro.runAndWait()

print(color.bLUE + "What do want to use?" + color.eND)
WhatDoYouWantToUse = pyttsx3.init()
WhatDoYouWantToUse.say("So Which service do want to use sir?")
WhatDoYouWantToUse.runAndWait()

recagnition(choice)
# IMPROVED SEARCH

time.sleep(1)
print(choice)

if "web" in choice:


    print(color.bLUE+"""What do you want to search?""" + color.eND)
    SearchWeb = pyttsx3.init()
    SearchWeb.say("What do you want to search")
    SearchWeb.runAndWait()

    time.sleep(2)
    print("")
    recagnition()
    time.sleep(1)

    recagnition(search)

    url = 'https://www.google.com/search?q='
    webbrowser.open(url + search)

    youtube_input = youtubee
    kit.playonyt(youtube_input)

##THE BRAND NEEW CALCULATOR
elif "calculator" in choice:
    print(color.bLUE+"""
What do you want to calculate?
Ex: Eight plus ten etc
    """+color.eND)
    CalculatorPre = pyttsx3.init()
    CalculatorPre.say("What do you want to calculate? As an example eight plus ten")
    CalculatorPre.runAndWait()

    recagnition(text)



    stringfinal = eval_binary_expr(*(text.split()))
    print(str(text) + color.rED+" IS EQUAL TO "+color.eND + str(stringfinal))
    say_final_calculator = str(text) + " is EQUAL TO " + str(stringfinal)
    Equal = pyttsx3.init()
    Equal.say(say_final_calculator)
    Equal.runAndWait()

##THE SHORTNER FROMM TOOL V1
elif "link" in choice:

    print(color.bLUE +"""
I will short the link you have copied and i will
print and copy the shortened link :)
    """ +color.eND)
    Shortner = pyttsx3.init()
    Shortner.say("I will shrink the link you have copied and i will copy it for you")
    Shortner.runAndWait()

    link = clip.paste()
    print(shortener.Shortener().clckru.short(link))
    clip.copy(shortener.Shortener().clckru.short(link))

    print(color.rED + """DONE :)""" + color.eND)


elif "YouTube" in choice:


    print( color.bLUE+ "Whats the name of the video?" +color.eND)

    Youtube_V = pyttsx3.init()

    Youtube_V.say("Whats the name of the video you want to play")

    Youtube_V.runAndWait()

    recagnition(youtubee)

    kit.playonyt(youtubee)



