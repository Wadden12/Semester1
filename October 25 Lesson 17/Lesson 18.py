# FileName: Lesson 18
# Mo's Quick Problems
# Author: Mike Wadden
# Date: October 26, 2021

import datetime


# Functions

def Celsius_to_Fahrenheit():
    """Calculator to Convert Celsius to Fahrenheit"""
    print()
    Celsius_Input = float(input("Enter a Celsius Temperature to be Converted to Fahrenheit: "))
    Fahrenheit = 9 / 5 * Celsius_Input + 32
    print(f"{Fahrenheit} Fahrenheit")
    print()
    AnyKey = input("Press any key to continue....")

def Pluto_Wife():
    """A Calculator to calculate the age of Pluto's ideal wife.
       She should be half his age plus 7 years"""
    print()
    Man_Age = int(input("Enter the Man's Age: "))
    print()
    Wife = round(Man_Age / 2 + 7)
    print(f"The Ideal Age of His Wife: {Wife}")
    print()
    AnyKey = input("Press any key to continue....")

def Training_Heart_Rate():
    """ Heart Training Calculator based on Agee And Resting Heart Rate"""
    print()
    Age = int(input("Enter Your Age: "))
    Resting_Heart = int(input("Enter the Resting Heart Rate: "))
    print()
    First_Cal = 220 - Age
    Second_Cal = First_Cal - Resting_Heart
    THR = (Second_Cal * .60) + Resting_Heart
    print(f"Training Heart Rate: {THR}")
    print()
    AnyKey = input("Press any key to continue....")


def Santa_Tracker():
    """ Santa Tracker: How many days until Christmas"""
    print()
    Christmas_day = datetime.date(year=2021, month=12, day=25)
    Days_Til_Christmas = (Christmas_day - datetime.date.today()).days
    if Days_Til_Christmas < 0:
        Days_Til_Christmas = int(Days_Til_Christmas) + 365

    print(F"Days Until Christmas: {Days_Til_Christmas}")
    print()
    AnyKey = input("Press any key to continue....")


def Find_My_Grade():
    """Allows users to input a grade between 0 and 100 and returns a Letter Grade"""
    print()
    while True:  # Loop to Ensure correct Grade is entered
        try:
            Grade = int(input("Enter a Grade between 0-100 to return a Letter Grade: "))
        except:
            print("Invalid Entry: Please use Numbers only between 0-100")
        else:
            if Grade < 0 or Grade > 100:
                print("Invalid Grade: Entry a grade between 0-100 ")
            else:
                print()
                if Grade >= 80:
                    print("A")
                    break
                elif Grade >= 70 and Grade <= 79:
                    print("B")
                    break
                elif Grade >= 60 and Grade <= 69:
                    print("C")
                    break
                elif Grade >= 50 and Grade <= 59:
                    print("D")
                    break
                else:
                    print("F")
                    break
    print()
    AnyKey = input("Press any key to continue....")


def How_Old_Invoice(Input_Date):
    """Function to check the Age of a Invoice and Return a Message"""
    Invoice_Age = (datetime.datetime.now() - Input_Date).days

    if Invoice_Age < 30:
        return print("OK")
    elif Invoice_Age >= 31 and Invoice_Age <= 60:
        return print("Better think about paying")
    else:
        return print("This one Could be Trouble")


def Guessing_Game():
    """Guessing Game"""

    import random

    Secret_Number = random.randint(1, 100)
    Guess_Counter = 0
    Guess = 0

    while Guess != Secret_Number:

        try:
            Guess = int(input("Guess a number between (1 and 100): "))
            Guess_Counter += 1

        except:
            print("Invalid Entry and A Guess was used:")

        else:

            if Guess < 1 or Guess > 100:
                print("Invalid Entry: Enter a number between 1-100 (This Counts as a Guess)")
            elif Guess > Secret_Number:
                print("Your Guess was to High")
            elif Guess < Secret_Number:
                print("You Guess was to Low")
            else:
                print(F"Your Guess is Correct and it took {Guess_Counter} Attempts ")




while True:
    # Menu Creation

    print()
    print("Mo's Quick Problems-Main Menu")
    print()
    print("1. Convert Celsius to Fahrenheit.")
    print("2. Plato's Ideal Wife.")
    print("3. Determine Training Heart Rate.")
    print("4. How many days to Christmas?")
    print("5. Find Letter Grade.")
    print("6. How old is an invoice.")
    print("7. Guessing Game.")
    print("8. Quit.")
    print()

    try:
        Choice = int(input(" Enter choice 1-8: "))

    except:
        print("Invalid Entry Please Enter a Number Between (1-8)")

    else:
        if Choice < 1 or Choice > 8:
            print("Invalid Entry Select a number Between 1-8")

        elif Choice == 1:  # Celsius to Fahrenheit Function
            Celsius_to_Fahrenheit()

        elif Choice == 2:  # Pluto's Ideal Wife Function
            Pluto_Wife()

        elif Choice == 3:  # Trainig Heart Rate Training
            Training_Heart_Rate()

        elif Choice == 4:  # Santa Tracker
            Santa_Tracker()

        elif Choice == 5:  # Number Grade to Letter Grade
            Find_My_Grade()

        elif Choice == 6: # Old Invoice Function
            print()
            while True:  # Date Validation Loop

                try:
                    Input_Date = input("Enter Invoice Date as (YYYY-MM-DD): ")
                    Invoice_Date = datetime.datetime.strptime(Input_Date, "%Y-%m-%d")
                except:
                    print("Invalid Date Entry. Re-Enter using (YYYY-MM-DD)")
                else:
                    if Invoice_Date > datetime.datetime.now():
                        print("Invalid Date: Cannot future Date Invoices ")
                    else:
                        How_Old_Invoice(Invoice_Date)
                        break
            print()
            AnyKey = input("Press any key to continue....")

        elif Choice == 7: #Guessing Game
            Guessing_Game()

        elif Choice == 8:  #Ends Program
            break
