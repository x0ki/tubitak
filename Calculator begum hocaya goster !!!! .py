from typing import List, Any, Union

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
            print("speak!...")
            text = r.recognize_google(audio)
        except:
            print("Sorry?")
    return text

condition = True

def substract(x,z):
    return x - z

def add(x,z):
    return x + z

def multiple(x,z):
    return  x * z

def divide(x,z):
    return x / z

print("""
Hi im the most simple calc uve ever seen :)
I cant handle more than two numbers :( 
Binan made me by the way :)
ooh i forgot u also can enter the numbers like;
 ( four ) instead of 4 maybe useless
 i just wanted to made it :)
""")

try:
    while condition == True:
        print("""
                    just choose the operation u want to do;
                    1 - Addition
                    2- Subtraction
                    3 - Multiplication
                    4- Division
                    ------> """)
        with sr.Microphone() as source:
            audio = r.listen(source)
            try:
                print("speak!...")
                choice1 = r.recognize_google(audio)
            except:
                print("Sorry?")
    choice = choice1




################################################## first
    print("Say the first number...")
    with sr.Microphone() as source:
            audio = r.listen(source)
            try:
                print("speak!...")
                spoken_numwor1 = r.recognize_google(audio)
            except:
                print("Sorry?")
    nums_as_words1 = spoken_numwor1
        #print("First number please >>> ")

    splitted_words1 = nums_as_words1.split(" ")
    num_dictioniry = {
            "zero": '0',
            "one": '1',
            "two": '2',
            "three": '3',
            "four": '4',
            "five": '5',
            "six": '6',
            "seven": '7',
            "eight": '8',
            "nine": '9',
            "ten": '10',
            "eleven": '11',
            "twelve": '12',
            "thirteen": '13',
            "fourteen": '14',
            "fifteen": '15',
            "sixteen": '16',
            "seventeen": '17',
            "eighteen": '18',
            "nineteen": '19',
            "twenty": '2',
            "thirty": '3',
            "fourty": '4',
            "fifty": '5',
            "sixty": '6',
            "seventy": '7',
            "eighty": '8',
            "ninety": '9',
            "hundred": '100'
    }
    output1 = ""
    for word1 in splitted_words1:
            output1 += num_dictioniry.get(word1, word1)

    first = int(output1)


####################################################         second
    print("Say the second number...")

    with sr.Microphone() as source:
            audio = r.listen(source)
            try:
                print("speak!...")
                spoken_numwor2 = r.recognize_google(audio)
            except:
                print("Sorry?")


    nums_as_words2 = spoken_numwor2

    splitted_words2 = nums_as_words2.split(" ")

    output2 = ""
    for word2 in splitted_words2:
        output2 += num_dictioniry.get(word2, word2)

        second = int(output2)


        if choice in ( "1" , "2" , "3" , "4", "add" , "substract" , "multiple" , "divide"):
            #first = float(input("please enter the first number --> "))
            #second = float(input("please enter the seconde number --> "))
            if choice == "1" or "add":
                result = add(first,second)
                print(first, "+", second, "=", result)
            elif choice == "2" or "substract":
                result = substract(first,second)
                print(first, " - ", second, " = ",result )
            elif choice == "3" or "multiple":
                result = multiple(first,second)
                print(first ," x " ,second , " = " , result)
            elif choice == "4" or "divide":
                result = divide(first,second)
                print(first , " / " , second ," = " ,result)
        else:
            print("Invalid input, TRY AGAIN!")
            exit()
except ValueError: print("\033[2;34;32m U just got a value error! propably u just did a mitake in the spelling!  \n")

