import operator
import SpeechRecog as sr
import webbrowser
import time
import pywhatkit as kit
import pyperclip as clip
import  pyshorteners as shortener

youtubee = ""
text = ""
choice = ""

sr.Microphone(device_index=1)
r = sr.Recognizer()

def recagnition():

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
        except:
            print("Sorry?")
    return text

#CALC .GET DEF,FUNCTION
def get_operator_fn(op):
    return {
        '+' : operator.add,
        '-' : operator.sub,
        'by' : operator.mul,
        'divided' :operator.__truediv__,
        '/' :operator.__truediv__,
        'Mod' : operator.mod,
        'mod' : operator.mod,
        '^' : operator.xor,
        }[op]

def eval_binary_expr(op1, oper, op2):
    op1,op2 = int(op1), int(op2)
    return get_operator_fn(oper)(op1, op2)



print("""
Hey sir its Binan!
Iam using google vioce reconition!
I can hear better than your wife!
Which service you want to use?
1 - VOICE ASSISTED WEB SEARCH
2 - VOICE ASSISTED CALCULATOR
3 - VOICE ASSISTED YOUTUBE SEARCH
4 - LINK SHORTNER

Ex:- Choose VOICE ASSISTED WEB SEARCH
MORE ASAP...
""")
time.sleep(8)
print("What do want to use?")

with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)
    try:
        choice = r.recognize_google(audio)
    except:
        print("Sorry?")


#IMPROVED SEARCH

time.sleep(1)
print(choice)

if "web" in choice:
    print("""What do you want to search?

    """)
    time.sleep(2)
    print("")
    recagnition()
    time.sleep(1)
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        try:
            search = r.recognize_google(audio)
        except:
            print("Sorry?")
    url = 'https://www.google.com/search?q='
    webbrowser.open(url + search)


    youtube_input = youtubee
    kit.playonyt(youtube_input)

##THE BRAND NEEW CALCULATOR
elif "calculator" in choice:
    print("""
What do you want to calculate?
Ex: Five plus eight etc
    """)
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
        except:
            print("Sorry?")

    print(text + " IS EQUAL TO ")
    stringfinal = eval_binary_expr(*(text.split()))
    print(stringfinal)

##THE SHORTNER FROMM TOOL V1
elif "link" in choice:
    print("""
I will short the link youve copied and i will
print and copy the shrtened link :)
    """)
    link = clip.paste()
    print(shortener.Shortener().clckru.short(link))
    clip.copy(shortener.Shortener().clckru.short(link))
    print("""DONE :)""")


elif "YouTube" in choice:
    print("Whats the name of the video?")


    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        try:
            youtubee = r.recognize_google(audio)
        except:
            print("Sorry?")

    kit.playonyt(youtubee)



