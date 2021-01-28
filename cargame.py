command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car is already STARTED!")
        else:
            started = True
            print("Car Started...")
    elif command == "stop":
        if not started:
            print("Car is already STOPPED.")
        else:
            started = False
            print("Car Stopped.")
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to escape the process""")
    elif command == "quit":
        break
    else:
        print("I don't understand you!")
