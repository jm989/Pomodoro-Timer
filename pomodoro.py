work = int(input("Enter work time: "))
rest = int(input("Enter rest time: "))

def check_rest():
    if rest != 5 or rest != 10 != 15:
        print("Rest times must either be 5, 10 or 15 minutes")

def checkWork():
    if work % 5 != 0:
        print("")