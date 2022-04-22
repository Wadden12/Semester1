# FileName: Lesson 26 R1
# ABC Customer Analysis: Menu
# Author: Mike Wadden
# Date: November 25, 2021

# Imports
from CustomerAnalysis import Customer_Analysis
from PaymentDays import Payment_Days
from CreditLimt import Credit_Limit
from PurchaseDays import Purchase_Days
from CustomerProv import Provice_Match
import time


while True:
    # Report Menu
    print()
    print(f"The ABC Company Report Menu")
    print()
    print("1. Customer Analysis Report")
    print("2. Customer Analysis Report: Over the credit limit")
    print("3. Customer Analysis Report: Have not made a purchase in 60 days")
    print("4. Customer Analysis Report: Have not made a payment in 30 days")
    print("5. Customer Analysis Report:By Province")
    print("6. Quit.")
    print()

    try:
        Choice = int(input(" Enter choice 1-6: "))

    except:
        print("Invalid Entry Please Enter a Number Between (1-6)")
    else:
        if Choice < 1 or Choice > 6:
            print("Invalid Entry Select a number Between 1-6")
        elif Choice == 1: # Customer Analysis Report Base
            Customer_Analysis()
        elif Choice == 2: # Credit Limit Report
            Credit_Limit()
        elif Choice == 3: # No Purchase in so many days
            Purchase_Days() # No Payments in so many days
        elif Choice == 4:
            Payment_Days()
        elif Choice == 5: # Province Report
            Provice_Match()
        elif Choice == 6: # Quit
            print()
            print("Closing Program ", end="")
            for wait in range(1, 11):
                print('*', end=' ')
                time.sleep(.2)
            print()

            break


