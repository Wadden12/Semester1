# Filename Main.py
# The Sprint Project Company Main Menu
# Authors:Cody Barrett, Gavin Coady, Mike Wadden.
# Date November 17, 2021

# Imports
import time
import datetime
# Functions

def As_Dollars_Pad(Number):
        """Format Dollars amounts to strings & Pad Right 10 Spaces"""
        Number_Display = f"${Number:,.2f}"
        Number_Display = f"{Number_Display:>10}"
        return Number_Display

def Number_Pad(Number):
        """Format Dollars amounts to strings & Pad Right 10 Spaces"""
        Number_Display = f"{Number:,}"
        Number_Display = f"{Number_Display:>10}"
        return Number_Display

def Write(Variable, f):
    """Function to Convert None Strings to Strings and Format to write to file with ,"""
    import datetime
    if isinstance(Variable, str) == False:
        if isinstance(Variable, datetime.datetime) == True:
            return f.write(f"{Variable.strftime('%Y-%m-%d')},")
        else:
            Variable = round(Variable, 2)
            return f.write(f"{str(Variable)},")
    elif isinstance(Variable, str) == True:
        return f.write(f"{(Variable)},")


def Write_Space(Variable, f):
    """Function to Convert None Strings to Strings and Format to write to file with Space"""
    import datetime
    if isinstance(Variable, str) == False:
        if isinstance(Variable, datetime.datetime) == True:
            return f.write(f"{Variable.strftime('%Y-%m-%d')}\n")
        else:
            Variable = round(Variable, 2)
            return f.write(f"{str(Variable)}\n")
    elif isinstance(Variable, str) == True:
        return f.write(f"{(Variable)}\n")

def Name_Validation(Name):
    """ Function to Validate a Name for Input: Allowing Spaces, - and '"""
    for Char in Name:
        if ("A" <= Char <= "Z" or "a" <= Char <= "z"
                or Char == "-" or Char == "'"):
            continue
        else:
            return False
    return True

def Business_Day(Date):
    """Function to Work Within Business Days Only Mon-Fri"""
    Weekday = Date.weekday()
    if Weekday == 5:
        Date += datetime.timedelta(days=2)
    elif Weekday == 6:
        Date += datetime.timedelta(days=1)
    return Date

# Part One Simple IPO Program

def Part_One():
    # CONSTANTS
    RENT_RATE = 35.00
    KM_RATE = 0.10
    HST_TAX = 0.15

    # INPUT STATEMENTS
    print()
    print("       Edsel Car Rental Company ")
    print()
    print("Please answer the following questions!")
    print()

    print("Rental Details")
    print()

    while True:
        try:
            Num_Days_Rented = int(input(" Number of days the automobile was rented: "))
        except:
            print("Invalid Entry: Please input a Number")
        else:
            if Num_Days_Rented == "":
                print("Cannot be blank! Please try again")
            elif Num_Days_Rented < 1:
                print("Invalid Entry Number Days Rented Cannot be Less than 1")
            else:
                break

    print()
    print("   Mileage")
    print()

    while True:
        try:
            Start_Mileage = int(input(" Starting mileage when car was rented: "))
            End_Mileage = int(input(" Ending mileage when car was returned: "))
        except:
            print("Invalid Entry: Please Input KM Amount")
        else:
            if Start_Mileage == "" or End_Mileage == "":
                print("Cannot be blank - Please try again!")
            elif Start_Mileage < 100:
                print("Invalid Entry Starting Mileage cannot be less than 100km")
            elif End_Mileage < Start_Mileage:
                print("Invalid Entry: Ending Mileage Cannot be less than starting Mileage")
            else:
                break
    print()
    AnyKey = input("Press any key to Display Rental Invoice....")
    print()

    # CALCULATIONS PROCESSING

    Km_Travelled = End_Mileage - Start_Mileage
    Daily_Cost = Num_Days_Rented * RENT_RATE
    Mileage_Cost = Km_Travelled * KM_RATE
    Rent_Cost = Daily_Cost + Mileage_Cost
    Tax_Cost = Daily_Cost * HST_TAX
    Total_Rent_Cost = Rent_Cost + Tax_Cost

    # CALCULATIONS FOR OUTPUT TO USER
    print()
    print("           Edsel")
    print("      Car Rental Company")
    print()
    print(" Mileage:")
    print("~" * 30)
    print(" Km's Travelled     {}".format(Number_Pad(Km_Travelled)))
    print("~" * 30)
    print(" Costs:")
    print("~" * 30)
    print(" Daily Cost         {}".format(As_Dollars_Pad(Daily_Cost)))
    print(" Mileage Cost       {}".format(As_Dollars_Pad(Mileage_Cost)))
    print(' ------------       {:>10}'.format("-" * 9))
    print(" Rental Cost        {}".format(As_Dollars_Pad(Rent_Cost)))
    print(" Tax/HST Cost       {}".format(As_Dollars_Pad(Tax_Cost)))
    print(' ------------       {:>10}'.format("-" * 9))
    print(" Total Cost         {}".format(As_Dollars_Pad(Total_Rent_Cost)))
    print("~" * 30)
    print()
    print()
    AnyKey = input("Press any key to Return to Menu....")
    print()
    print("Loading ", end="")
    for wait in range(1, 11):
        print('*', end=' ')
        time.sleep(.2)
    print()
    return

# Option 2 If and Loop Sample

def FizzBuzz(X=5,Y=8):
    """Number Divisible by 5 = Fizz and Number Divisible by 8 = Buzz, both = FizzBuzz"""
    for Number in range(1, 101):

        Fizz = Number % X
        Buzz = Number % Y

        if Fizz == 0 and Buzz == 0:
            print("FizzBuzz")
        elif Fizz == 0:
            print("Fizz")
        elif Buzz == 0:
            print("Buzz")

        else:
            print(Number)
    print()
    AnyKey = input("Press any key to Return to Menu....")
    print()
    print("Loading ", end="")
    for wait in range(1, 11):
        print('*', end=' ')
        time.sleep(.2)
    print()
    return

# Strings and Dates

def Part_Three():
    # inputs
    print()
    print("Employee Information Page")
    print()

    while True:
        First = input("First Name: ").title().lstrip().rstrip()
        if First == "":
            print("First Name cannot be blank: Please Re-Enter")
        elif len(First) > 25:
            print("Invalid First Name Length: Cannot be longer than 25 letters ")
        elif Name_Validation(First) == False:  # Function to Validate Name Input
            print("Invalid Name Entered: Please use letters between (a-z), (-) and (') No Spaces")
        else:
            break

    while True:
        Last = input("Last Name: ").title().lstrip().rstrip()
        if Last == "":
            print("Last Name cannot be blank: Please Re-Enter")
        elif len(Last) > 30:
            print("Invalid Last Name Length: Cannot be longer than 30 letters ")
        elif Name_Validation(Last) == False:  # Function to Validate Name Input
            print("Invalid Name Entered: Please use letters between (a-z), (-) and (') ")
        else:
            break

    while True:
        try:
            StartDate = input("What date did they start? (YYYY-MM-DD): ")
            StartDate = datetime.datetime.strptime(StartDate, "%Y-%m-%d")
        except:
            print("Invalid start date - must be in the format YYYY-MM-DD).")
        else:
            break

    while True:
        try:
            BirthDate = input("What is the Employee's Birthday? (YYYY-MM-DD): ")
            BirthDate = datetime.datetime.strptime(BirthDate, "%Y-%m-%d")
        except:
            print("Invalid Birthdate - must be in the format YYYY-MM-DD).")
        else:
            break

    while True:
        try:
            Salary = int(input("What is their yearly salary?: "))
        except:
            print("Invalid Entry: Please input the Yearly Salary")
        else:
            if Salary <= 0:
                print("Salary must be greater than 0!")
            else:
                break

    # Forrmatting and Calculations

    StartDateStr = str(StartDate)
    BirthDateStr = str(BirthDate)
    EmployeeNo = f"{First[0]}{Last[0]}-{StartDateStr[0:4]}-{BirthDateStr[5:7]}"
    ReviewDate = StartDate + datetime.timedelta(weeks=52)
    Probation = StartDate + datetime.timedelta(days=90)

    # days to next birthday

    Today = datetime.date.today()
    if (Today.month == BirthDate.month and Today.day >= BirthDate.day or Today.month > BirthDate.month):
        NextBirthdayYear = Today.year + 1
    else:
        NextBirthdayYear = Today.year

    NextBirthday = datetime.date(NextBirthdayYear, BirthDate.month, BirthDate.day)

    DaysToNextBirthday = NextBirthday - Today

    if (Today.month == StartDate.month and Today.day >= StartDate.day or Today.month > StartDate.month):
        NextReviewYear = Today.year + 1
    else:
        NextReviewYear = Today.year

    NextReview = datetime.date(NextReviewYear, StartDate.month, StartDate.day)

    # Output
    print()
    print("Employee Information:")
    print()
    print(f"Employee Name: {First} {Last}; {First[0].title()}.{Last}; {Last},{First[0]}.")
    print("Employee Number: ", EmployeeNo)
    print(f"Employee Review Date: {ReviewDate.strftime('%Y-%m-%d')}")
    print("Days left to Employee's next Birthday:", DaysToNextBirthday.days)
    print(f"Salary: ${Salary:,}")
    print()
    print(f"{EmployeeNo}:({First} {Last})")
    print("-" * 50)
    if ReviewDate > datetime.datetime.now():
        print(f"Next Annual Review Date:         {Business_Day(ReviewDate.date())}")
    else:
        print(f"Next Annual Review Date:         {Business_Day(NextReview)}")
    print(f"Probation Period End:            {Probation.strftime('%Y-%m-%d')}")
    print()
    print(f"Eligible for company benefits on: {Probation.strftime('%B %d, %Y')} ")

    print()
    AnyKey = input("Press any key to Return to Menu....")
    print()
    print("Loading ", end="")
    for wait in range(1, 11):
        print('*', end=' ')
        time.sleep(.2)
    print()
    return

#Option 4 Data Files and Default Values.

def Part_Four():
    # opening Default values from file
    with open('ECRDef.dat', 'r') as f:
        RENTAL_NUMBER = int(f.readline())
        RENT_RATE = int(f.readline())
        KM_RATE = float(f.readline())
        TAX = float(f.readline())

    while True: #Program end loop

        # INPUT STATEMENTS
        print()
        print("       Edsel Car Rental Company ")
        print()
        print("Please answer the following questions")
        print()
        print("*" * 40)
        print(" To End Program and Return to Menu ")
        print("      Enter 0 for Travel Days")
        print("*" * 40)
        print()
        print(" Rental Details")
        print()

        while True:
            try:
                Num_Days_Rented = int(input(" Number of days the automobile was rented: "))
            except:
                print("Invalid Entry: Please input a Number")
            else:
                if Num_Days_Rented == 0:
                    print()
                    print("Loading ", end="")
                    for wait in range(1, 11):
                        print('*', end=' ')
                        time.sleep(.2)
                    print()
                    break
                elif Num_Days_Rented < 0:
                    print("Invalid Entry Number Days Rented Cannot be Less than 0")
                else:
                    break
        if Num_Days_Rented == 0:
            break

        print()
        print("   Mileage")
        print()

        while True:
            try:
                Start_Mileage = int(input(" Starting mileage when car was rented: "))
                End_Mileage = int(input(" Ending mileage when car was returned: "))
            except:
                print("Invalid Entry: Please Input KM Amount")
            else:
                if Start_Mileage == "" or End_Mileage == "":
                    print("Cannot be blank - Please try again!")
                elif Start_Mileage < 100:
                    print("Invalid Entry Starting Mileage cannot be less than 100km")
                elif End_Mileage < Start_Mileage:
                    print("Invalid Entry: Ending Mileage Cannot be less than starting Mileage")
                else:
                    break
        print()
        AnyKey = input("Press any key to Display Rental Invoice....")
        print()

        # CALCULATIONS PROCESSING

        Km_Travelled = End_Mileage - Start_Mileage
        Daily_Cost = Num_Days_Rented * RENT_RATE
        Mileage_Cost = Km_Travelled * KM_RATE
        Rent_Cost = Daily_Cost + Mileage_Cost
        Tax_Cost = Daily_Cost * TAX
        Total_Rent_Cost = Rent_Cost + Tax_Cost

        # CALCULATIONS FOR OUTPUT TO USER
        print()
        print("      Edsel Car Rental Company ")
        print(f"          Rental Number")
        print(f"              #{RENTAL_NUMBER}")
        print()
        print(" Mileage:")
        print("~" * 30)
        print(" Km's Travelled     {}".format(Number_Pad(Km_Travelled)))
        print("~" * 30)
        print(" Costs:")
        print("~" * 30)
        print(" Daily Cost         {}".format(As_Dollars_Pad(Daily_Cost)))
        print(" Mileage Cost       {}".format(As_Dollars_Pad(Mileage_Cost)))
        print(' ------------       {:>10}'.format("-" * 9))
        print(" Rental Cost        {}".format(As_Dollars_Pad(Rent_Cost)))
        print(" Tax/HST Cost       {}".format(As_Dollars_Pad(Tax_Cost)))
        print(' ------------       {:>10}'.format("-" * 9))
        print(" Total Cost         {}".format(As_Dollars_Pad(Total_Rent_Cost)))
        print("~" * 30)
        print()

        # writing Data onto Rentals.dat
        with open('Rentals.dat', 'a') as f:
            Write(RENTAL_NUMBER, f)
            Write(Num_Days_Rented, f)
            Write(Start_Mileage, f)
            Write(End_Mileage, f)
            Write(Km_Travelled, f)
            Write(Daily_Cost, f)
            Write(Mileage_Cost, f)
            Write(Rent_Cost, f)
            Write(Tax_Cost, f)
            Write_Space(Total_Rent_Cost, f)

        print()
        print("Entry Have been Saved")
        print()
        # Adding to Rental Number:
        RENTAL_NUMBER += 1
        print()
        AnyKey = input("Press any key to Continue....")
        print()

    # Writes the Defaults back to File with the changed Rental Number
    with open('ECRDef.dat', 'w') as f:
        Write_Space(RENTAL_NUMBER, f)
        Write_Space(RENT_RATE, f)
        Write_Space(KM_RATE, f)
        Write_Space(TAX, f)
    return

while True:
    # Main Menu
    print()
    print(f"The Sprint Project Company")
    print()
    print("1. Simple IPO Program.")
    print("2. If and Loop Sample.")
    print("3. Strings and Dates.")
    print("4. Data files and Default Values")
    print("5. Quit.")
    print()

    try:
        Choice = int(input(" Enter choice 1-5: "))

    except:
        print("Invalid Entry Please Enter a Number Between (1-5)")
    else:
        if Choice < 1 or Choice > 5:
            print("Invalid Entry Select a number Between 1-5")
        elif Choice == 1:  # Simple IPO Program
            Part_One()
        elif Choice == 2:  # If and Loop Sample
            FizzBuzz()
        elif Choice == 3:  # Strings and Dates
            Part_Three()
        elif Choice == 4:  # Data files and Default Values
            Part_Four()
        elif Choice == 5: # Quit
            print()
            print("Closing Program ", end="")
            for wait in range(1, 11):
                print('*', end=' ')
                time.sleep(.2)
            print()

            break
