import time

def pomodoro_timer():
    print("Choose a work duration:")
    print("1. 30 minutes")
    print("2. 60 minutes")
    print("3. 90 minutes")
    print("4. 120 minutes")

    while True:
        choice = input("Enter your choice (1/2/3/4): ")
        if choice in ['1', '2', '3', '4']:
            break
        else:
            print("Invalid choice. Please enter a valid option.")
    
    choice = int(choice)

    if choice == 1:
        duration = 30
    elif choice == 2:
        duration = 60
    elif choice == 3:
        duration = 90
    else:
        duration = 120

    print(f"Timer set for {duration} minutes.")
    workTimer(duration)
    rest_duration = select_rest_duration()
    print(f"Starting rest timer for {rest_duration} minutes rest..")
    restTimer(rest_duration)

    # Code to start the timer with the selected duration goes here

def workTimer(duration):
    for x in range(duration * 60, 0, -1):
        seconds = x % 60
        minutes = int(x / 60) % 60
        hours = int(x / 3600) 
        print(f"{hours:02}:{minutes:02}:{seconds:02}")
        time.sleep(1)
    
    print("Take a break")

def restTimer(duration):
        for x in range(duration * 60, 0, -1):
            seconds = x % 60
            minutes = int(x / 60) % 60
            hours = int(x / 3600) 
            print(f"{hours:02}:{minutes:02}:{seconds:02}")
            time.sleep(1)
        
        print("Back to work")

def select_rest_duration():
    print("Choose a rest duration:")
    print("1. 5 minutes")
    print("2. 10 minutes")
    print("3. 15 minutes")
    print("4. 20 minutes")

    while True:
        choice = input("Enter your choice (1/2/3/4): ")
        if choice in ['1', '2', '3', '4']:
            break
        else:
            print("Invalid choice. Please enter a valid option.")

    choice = int(choice)  # Convert the choice to an integer

    if choice == 1:
        rest_duration = 5
    elif choice == 2:
        rest_duration = 10
    elif choice == 3:
        rest_duration = 15
    else:
        rest_duration = 20

    return rest_duration
pomodoro_timer()
