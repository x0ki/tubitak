nothing = 1
Status = False
##Zero means the engine is off 1 is on 2 Brake
print("Hi if u r not fa god of atheists just type help :)")
command = ""

while nothing == 1:
    command = input("Whats the command commerade? ->").lower()
    if command == "help":
        print("""
            Start:To start the engine and go 
            Stop:To hold brakes turn the engine off
            Quit:To leave me alone...
            Help:Do i have to explain it?
        """)
    elif command == "start" :
       if Status is False:
           print("- Vehicle started commerade - ")
           Status = True
       else:
           print("- The engine is already on -")

    elif command == "stop" :
        if Status is True:
            print("We stopped and the engine is off commerade!")
            Status = False
        else:
            print("The engine is already off")


    elif command == "quit":
        print("So u gonna leve me alone?")

        break
    else:
        print("Commerade Stalin wont allow that! i cant see the command in our book!")