# FileName: Lesson 16
# Insurance Company Program
# Author: Mike Wadden
# Date: October 26, 2021

#Constants

HOME_POLICY = 400
AUTO_POLICY = 700
BOTH_POLICY = 1000
RENEWAL_DIS = .10   # 10% for renewed policies
EXTRA_LIABILITY = 75
EXTRA_PERSON = 90
CONTENT_INSURANCE = 110
TAX_RATE = .15
INTEREST_RATE = 0.054
PROCESSING_FEE = 47.95
MONTH = 8               # 8 month payments
TERMS_DIS = 0.02        # 2% discount if the bill is paid in 10 days or less

# Imports

import datetime
import random

def As_Dollars(Number):
    """Format Dollars amounts to strings"""
    Number_Display = f"${Number:,.2f}"
    return Number_Display


Extra_Cost = 0    #Set Extra Cost to 0 to be used in a logic statements

Policy_Date = "2021-07-25"
Policy_Date = datetime.datetime.strptime(Policy_Date, "%Y-%m-%d").date()

First_Name = "Michael"
Last_Name = "Wadden"
Street_Address = "44 Kenai Cresent"
City = "St.John's"
Province = "NL"
Postal_Code = "A1A5A5"
Home_Phone = "7097262539"
Cell_Phone = "7097432738"
Work_Phone = "7093641444"

while True:
    Policy = input("New Policy or Renewal? (N)ew or (R)enewal: ").upper()
    if Policy == "R":
        Policy_Message = "(10% reduction for policy renewal)"
        Discount = RENEWAL_DIS
        break
    elif Policy == "N":
        Policy_Message = ""
        Discount = 0
        break
    else:
        print("Invalid Input: Please Enter (N) for New or (R) for Renewal: ")

while True:
    Policy_Type = input("Select a Policy: (H)ome, (A)uto, or (B)oth: ").upper()
    if Policy_Type == "H":
        Base_Policy = HOME_POLICY
        break
    elif Policy_Type == "A":
        Base_Policy = AUTO_POLICY
        break
    elif Policy_Type == "B":
        Base_Policy = BOTH_POLICY
        break
    else:
        print("Invalid Input: Please Enter (H) for Home or (A) for Auto or (B) for Both: ")

print()
print("Input (Y) for Yes and (N) for No: On the Follow Extra Options:")
print()

while True:
    Liability = input("Extra Liability: ").upper()

    if Liability == "Y":
        Extra_Cost += EXTRA_LIABILITY
        break
    elif Liability == "N":
        break
    else:
        print("Invalid Input: Please Enter (Y) for Yes or (N) for No: ")

while True:
    Extra_Person_Coverage = input("Extra Person Coverage: ").upper()

    if Extra_Person_Coverage == "Y":
        Extra_Cost += EXTRA_PERSON
        break
    elif Extra_Person_Coverage == "N":
        break
    else:
        print("Invalid Input: Please Enter (Y) for Yes or (N) for No: ")

while True:
    Content = input("Content Insurance: ").upper()

    if Content == "Y":
        Extra_Cost += CONTENT_INSURANCE
        break
    elif Content == "N":
        break
    else:
        print("Invalid Input: Please Enter (Y) for Yes or (N) for No: ")

# Processing

Base_Policy = Base_Policy * (1-Discount)      #Works out Base Policy and Discounted Base Policy baed on Policy Selection
Sub_Total = Base_Policy + Extra_Cost
Hst = Sub_Total * TAX_RATE
Policy_Total = Sub_Total + Hst
Term_Discount = Sub_Total * TERMS_DIS
Interest = Policy_Total * INTEREST_RATE * (MONTH/12)
Final_Total = Policy_Total + Interest + PROCESSING_FEE

#Date Processing

Ten_Days = Policy_Date + datetime.timedelta(days = 10)
Forty_Five_Days = Policy_Date + datetime.timedelta(days = 45)
First_Payment = Policy_Date + datetime.timedelta(days = 30)
Policy_date_Str = str(Policy_Date)
Random_Number = str(random.randint(100, 999))
Monthly_Payment = Final_Total / MONTH

# Policy Number

Policy_Number = f"{First_Name[0]}{Last_Name[0]}-{Policy_date_Str[0:4]}-{Random_Number}"

#Output

print()
print(F"{'ONE STOP INSURANCE':30}{Policy_Date.strftime('%d-%b-%y'):>11}")
print(F"{'CUSTOMER POLICY SUMMARY':30}{Policy_Number:>11}")
print("-" * 41)
print(F"Client: {First_Name[0]}.{Last_Name}")
print(F"{' ' * 8}{Street_Address}")
print(F"{' ' * 8}{City}, {Province} {Postal_Code}")
print()
print(F"{'Policy base cost:':30}{As_Dollars(Base_Policy):>11}")
print(F"  {Policy_Message}")
print(F"{'Extra cost:':30}{As_Dollars(Extra_Cost):>11}")
print(F"{'Subtotal:':30}{As_Dollars(Sub_Total):>11}")
print(F"{'HST:':30}{As_Dollars(Hst):>11}")
print(F"{' '* 30}{'-' * 9:>11}")
print(F"{'Policy total':30}{As_Dollars(Final_Total):>11}")
print()
print("For Monthly payment customers:")
print(F"   {'Monthly payment:':27}{As_Dollars(Monthly_Payment):>11}")
print(F"   {'First payment date:':27}{First_Payment.strftime('%d-%b-%y'):>11}")
print()
print("For payment in full:")
print(F"   {'Discount date:':27}{Ten_Days.strftime('%d-%b-%y'):>11}")
print(F"   {'Discount amount:':27}{As_Dollars(Term_Discount):>11}")
print(F"   {'Full payment date:':27}{Forty_Five_Days.strftime('%d-%b-%y'):>11}")
print("-" * 41)
print(" " * 4,'"ONE STOP - Insuring the world!"')