# FileName: Lesson 15 Q3
# Tracking code problem: String methods
# Author: Mike Wadden
# Date: October 19, 2021

import datetime
import random

#Inputs

# Current Date
Date = str(datetime.datetime.now( ).date())

while True:
    First_Name = input("Customer First Name: ").title()
    if First_Name == "":
        print("First Name cannot be Blank: Please re-enter")
    else:
        break

while True:
    Last_Name = input("Customer Last Name: ").title()
    if Last_Name == "":
        print("Last Name cannot be Blank: Please re-enter")
    else:
        break


while True:
    Location_Code = input("Input 4 Letter Location Code: ").upper()
    if len(Location_Code) != 4:
        print("Invalid Entry. Please Entry the 4 Letter Code: ")
    elif Location_Code.isalpha() == False:
        print("Invalid Entry. Please Entry the 4 Letter Code: ")
    else:
        break

while True:
    try:
        Transit_Code = int(input("Enter 5 Number Transit Code: "))
    except:
        print("Invalid Entry: Input must be a Integer:")
    else:
        Transit_Code = str(Transit_Code)
        if len(Transit_Code) == 5:
            break
        else:
            print("Invalid Entry: Input Must be 5 Numbers")

#Random Generate number for customer Counter

Customer_Counter = str(random.randint(1000, 9999))


#output

print(f" Tracking #: {First_Name[0] + Last_Name[0]}-{Location_Code[0:2]}-{Transit_Code[3:5]}-{Date[0:4] + Customer_Counter[0:4]}")











