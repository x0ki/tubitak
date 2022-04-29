
import speech_recognition as sr
import webbrowser
import time

sr.Microphone(device_index=1)
r = sr.Recognizer()
r.energy_threshold = 6000

def recagnition():

    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
        except:
            print("Sorry?")
    return text

print("""
Hey sir its Binan!
Iam using google vioce reconition!
I can hear better than your wife!
Which service you want to use?
1 - VOICE ASSISTED WEB SEARCH
2 - VOICE ASSISTED CALCULATOR
3 - VOICE ASSISTED YOUTUBE SEARCH
Ex:- Choose the first one
Ex:- Choose VOICE ASSISTED WEB SEARCH
MORE ASAP...
""")
time.sleep(10)
print("")

recagnition()
choice = recagnition()


time.sleep(2)
if "first" or "web" or "search" in choice:
    print("What do you want to search?")
    time.sleep(2)
    print("")
    recagnition()
    time.sleep(1)
    search = recagnition()
    url = 'https://www.google.com/search?q='
    webbrowser.open(url + search)

