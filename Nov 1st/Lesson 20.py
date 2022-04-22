# Filename = Lesson 9 Q1
#  NL Chocolate Company: Salesperson Travel Claim Forum Calculation
# Author Mike Wadden
# Date Septmeber 23, 2021

# Constants

PERDEIM_RATE1 = 85                     # Per deim rate of $85 per day when traveling 3 or less days
PERDEIM_RATE2 = 100                    # Per deim rate of $100 per day when traveling 4 or more days
KM_RATE = 0.10                         # 10 cent  rate per KM  when using sales rep own car
RENTAL_RATE = 56                       # $56 per day when using a rental car
COMPANY_NAME = "NL Chocolate Company"

# Open Default File and read values into Variables
f = open('Def.txt', 'r')
CLAIM_NUMBER = int(f.readline())
TAX = float(f.readline())
f.close()

# Imports
import sys

# Functions

def Write_Space(Variable, f):
    """Function to Convert None Strings to Strings and Format to write to file with Space"""
    import datetime
    if isinstance(Variable, str) == False:
        if isinstance(Variable, datetime.datetime) == True:
            return f.write(f"{Variable.strftime('%Y-%m-%d')}\n")
        else:
            return f.write(f"{str(Variable)}\n")
    elif isinstance(Variable, str) == True:
        return f.write(f"{(Variable)}\n")


def Name_Validation(Name):
    """ Function to Validate a Name for Input: Allowing Spaces, - and '"""
    for Char in Name:
        if ("A" <= Char <= "Z" or "a" <= Char <= "z" or Char == " "
                or Char == "-" or Char == "'"):
            continue
        else:
            return False
    return True

def Date_Change(Date):
    """Convert Date input (YYYY-MM_DD) into a datetime object"""
    import datetime
    Date = datetime.datetime.strptime(Date, "%Y-%m-%d")
    return Date

# User Inputs

while True:

    print("Travel Claim Forum input")
    print()
    while True:

        print('Input "END" into the Employee Number to Close Program')
        print()
        Employee_Number = input("Enter The Three Digit Employee's Number: ").upper().rstrip().lstrip()

        if len(Employee_Number) != 3:
            print("Employee Number is Incorrect. Please Key the 3 digit Number")
        elif Employee_Number.upper() == "END":
            print("Good Bye")
            break
        else:
            break

    if Employee_Number.upper() == "END":
        break

    while True:

        Employee_Name = input("Enter Employee Name: ").title().lstrip().rstrip()

        if Employee_Name == "":
            print("Name cannot be blank: Please Re-Enter")

        elif Name_Validation(Employee_Name) == False:  # Function to Validate Name
            print("Invalid Name Entered: Please use letters between (a-z), (-) and (') ")
        else:
            break

    Trip_Location = input("Trip Location: ")

    while True:  # Date Validation Loop
        try:
            Start_Date = input("Enter Start Date as (YYYY-MM-DD): ")
            Start_Date = Date_Change(Start_Date)
            End_Date = input("Enter End Date as (YYYY-MM-DD): ")
            End_Date = Date_Change(End_Date)
        except:
            print("Invalid Date Entry. Re-Enter using (YYYY-MM-DD)")
        else:
            if End_Date < Start_Date:
                print("Invalid Entry: The End Date Cannot be before the End Date: ")
            else:
                break

    Travel_Days = (End_Date - Start_Date).days    #Calculate the Travel Days

    if Travel_Days <= 3 :
        Perdeim = PERDEIM_RATE1 * Travel_Days
    else:
        Perdeim = PERDEIM_RATE2 * Travel_Days

    while True:
        Car = input("Enter (O) for Own Car or (R) for Rental: ").upper()
        if Car == "":
            print("Invlaid Entry: Please Enter (O) for Own Car or (R) for Rental) ")
        elif Car == "O":
            KM_Total = int(input("Total KM Traveled: "))
            Vehicle_Allowance = KM_Total * KM_RATE
            Transportation = "The Salesperson Used Their Own Car"
            KM_Dis = "and Traveled: {:,}km".format(KM_Total)
            break
        elif Car == "R":
            Vehicle_Allowance = RENTAL_RATE * Travel_Days
            Transportation = "The Salesperson Used a Rental Car"
            KM_Dis = " "
            break
        else:
            print("Incorrect Value entered, Please Enter O or R")

    # Processing Calculations

    Subtotal = Perdeim + Vehicle_Allowance
    Hst = Perdeim * TAX
    Total_Claim = Subtotal + Hst

    #Format for Output
    Vehicle_Allowance_Dis = "${:,.2f}" .format(Vehicle_Allowance)
    Perdeim_Dis = "${:,.2f}" .format(Perdeim)
    Hst_Dis = "${:,.2f}" .format(Hst)
    Total_Claim_Dis = "${:,.2f}" .format(Total_Claim)
    Subtotal_Dis = "${:,.2f}" .format(Subtotal)

    #OutPut for User to see

    print()
    print(COMPANY_NAME.center(60))
    print(" " * 23, "Travel Claim", "#", CLAIM_NUMBER)
    print()
    print(" " * 2, "Employee number: {:<.3}       Employee Name: {:<.20}".format(Employee_Number.upper(), Employee_Name.title()))
    print()
    print(" " * 2, "{:18}  {:12}  {:<20}" .format("Trip Location:", "Start Date:", Start_Date.strftime('%Y, %m %d')))
    print(" " * 2, "{:18}  {:12}  {:<20}" .format(Trip_Location, "End Date:", End_Date.strftime('%Y, %m %d')))
    print()
    print(" " * 2, "*" * 59)
    print(" " * 2, " {} {} ".format(Transportation, KM_Dis))
    print(" " * 2, "*" * 59)
    print()
    print(" " * 2, "{:12} {:<12}" .format("Per Diem", Perdeim_Dis))
    print(" " * 2, "{:12} {:<12}" .format("Vehicle", Vehicle_Allowance_Dis))
    print(" " * 2, "{:12} {:<12}" .format("Subtotal", Subtotal_Dis))
    print(" " * 2, "{:12} {:<12}" .format("HST", Hst_Dis))
    print(" " *2, "-" * 25)
    print(" " * 2, "{:12} {:<12}" .format("Total Claim", Total_Claim_Dis))
    print()

    # Writing the OutPut to a file
    original_stdout = sys.stdout
    with open('Claims.txt', 'a') as f:
        sys.stdout = f
        print()
        print(COMPANY_NAME.center(60))
        print(" " * 23, "Travel Claim", "#", CLAIM_NUMBER)
        print()
        print(" " * 2, "Employee number: {:<.3}       Employee Name: {:<.20}".format(Employee_Number.upper(),
                                                                                     Employee_Name.title()))
        print()
        print(" " * 2, "{:18}  {:12}  {:<20}".format("Trip Location:", "Start Date:", Start_Date.strftime('%Y, %m %d')))
        print(" " * 2, "{:18}  {:12}  {:<20}".format(Trip_Location, "End Date:", End_Date.strftime('%Y, %m %d')))
        print()
        print(" " * 2, "*" * 59)
        print(" " * 2, " {} {} ".format(Transportation, KM_Dis))
        print(" " * 2, "*" * 59)
        print()
        print(" " * 2, "{:12} {:<12}".format("Per Diem", Perdeim_Dis))
        print(" " * 2, "{:12} {:<12}".format("Vehicle", Vehicle_Allowance_Dis))
        print(" " * 2, "{:12} {:<12}".format("Subtotal", Subtotal_Dis))
        print(" " * 2, "{:12} {:<12}".format("HST", Hst_Dis))
        print(" " * 2, "-" * 25)
        print(" " * 2, "{:12} {:<12}".format("Total Claim", Total_Claim_Dis))
        print()
        sys.stdout = original_stdout
    print()
    print("The Entry Has been Saved")
    print()

    CLAIM_NUMBER += 1 #Updates the Claim Number
    f = open('Def.txt', 'w')
    Write_Space(CLAIM_NUMBER, f)
    Write_Space(TAX, f)
    f.close()


    while True: #Secondary Exit for the Program
        Continue = input("Do you want to make another Entry?  (Y) or (N) ")
        if Continue.upper() == "Y":
            break
        elif Continue.upper() == "N":
            print()
            Employee_Number = "END"
            break
        else:
            print("Incorrect Value entered, Please Enter Y or N")

    if Employee_Number == "END":
        print()
        print("Good Bye")
        print()
        break