command = ""
car_running = 0
print ("welcome to car game")
print ("type (h)elp to get a list of commands")
while True:
    command = input("> ")
    if  command == "h":
        print ("(h)elp")
        print ("(s)tart car")
        print ("s(t)op car")
        print ("(e)xit game")
        print ("")
        command = ""
    elif command == "s" and car_running == 0:
        print ("car is now running")
        print ("ready to go...")
        car_running = 1
        command = ""
    elif command == "s" and car_running == 1:
        print ("car has already been started")
        command = ""
    elif command == "t" and car_running == 1:
        print ("car has been stopped")
        car_running = 0
        command = ""
    elif command == "t" and car_running == 0:
        print ("car wasn't running")
        command = ""
    elif command == "e":
        break 
    else:
        print ("that command doesn't exist")
        print ("type (h)elp for list of commands")
        command = ""
print("game has been ended")