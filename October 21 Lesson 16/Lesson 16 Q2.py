# FileName: Lesson 16 Q1
# Company Invoice Discount Calculator
# Author: Mike Wadden
# Date: October 21, 2021

# Constants

DISCOUNT_RATE = 0.02

# Imports

import datetime

# Inputs

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
            break

while True:  #Invoice Total Check
    try:
        Invoice = float(input("Enter the Invoice Total: $"))
    except:
        print("Invalid Entry: Please Enter a Number Value: ")
    else:
        break

#Processing

Ten_Days = Invoice_Date + datetime.timedelta(days = 10)
Thirty_Days = Invoice_Date + datetime.timedelta(days= 30)
Invoice_Age = (datetime.datetime.now() - Invoice_Date)

#Discount Processing
Terms_Discount = Invoice * DISCOUNT_RATE
Discount = Invoice - Terms_Discount

#Output
print()
print(f"Invoice Total: ${Invoice:,.2f}, Invoice Date: {Invoice_Date.date}")
print("*" * 50)
print("Terms: 2/10 N30")
print("*" * 25)
print(f"Discount Date: {Ten_Days.date()}: Discount Total: ${Discount:,.2f}")
print("*" * 50)
print(f"Invoice Due Date: {Thirty_Days.date()}")
print("*" * 34)
print(f"The Invoice is Currently {Invoice_Age.days} days old")
print("*" * 34)

