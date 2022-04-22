# FileName: Lesson 16 Q1
# Company Per Doem Calculator
# Author: Mike Wadden
# Date: October 21, 2021

# Costants:

PER_DIEM = 56

# imports

import datetime

# Inputs:

while True:
    try:
        Start_Date = input("Enter Start Date: using (dd-mm-yyyy) format ")
        Arrival = datetime.datetime.strptime(Start_Date, "%d-%m-%Y")
        End_Date = input("Enter End Date: using (dd-mm-yyyy) format ")
        Depart = datetime.datetime.strptime(End_Date, "%d-%m-%Y")
    except:
        print("Invalid Date Entry. Re-Enter using (dd-mm-yyyy)")
    else:
        if Depart < Arrival:
            print("Invalid Entry: End Date Cannot be before Start Date: ")
        else:
            break


# processing

Travel_Days = (Depart - Arrival).days
Allowance = Travel_Days * PER_DIEM


print(f"Total Allowance for the Trip is ${Allowance:,.2f} ")

