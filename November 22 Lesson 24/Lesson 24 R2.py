# FileName: Lesson 24 R2
# Accounts Accounts Receivable Summary Report
# Author: Mike Wadden
# Date: November 22, 2021

def As_Dollars(Number):
    """Format Dollars amounts to strings"""
    Number_Display = f"${Number:,.2f}"
    return Number_Display

import datetime
Today = datetime.datetime.now().date()
# Headings top of the report
print("                      Widgits Incorporated")
print()
print(f"{'       ACCOUNT RECEIVABLE SUMMARY REPORT AS OF'} {Today.strftime('%m-%d-%Y')}")
print()
print(f"{'ACCOUNT':12}{'  CUSTOMER':18}{' BALANCE':10}{'   CREDIT':13}{'  MINIMUM':10}")
print(f"{'NUMBER':12}{'    NAME':18}  {' DUE':10}{'REMAINING':13}{'PAYMENT':10}")
print("=" * 64)

Cus_Count = 0
BalDueAcc = 0
MinPayAcc = 0
# Report Details
f = open("Customers.dat", "r")
for CustomerData in f:
    CustomerLine = CustomerData.split(",")
    Account_Number = CustomerLine[0]
    Customer_Name = CustomerLine[1].strip()
    Balance_Due = float(CustomerLine[5].strip())
    Credit_limit = float(CustomerLine[6].strip())

    Credit_Remain = Credit_limit - Balance_Due
    Cus_Count += 1
    BalDueAcc += Balance_Due
    if Credit_Remain < 0:
        Min_Payment = (Balance_Due * .10) + (Credit_Remain * -1)
        MinPayAcc += Min_Payment
    else:
        Min_Payment = Balance_Due * .10
        MinPayAcc += Min_Payment
    # don't use pad for spacing in the future just pad it for the size of the number
    print(f"{Account_Number:8} {Customer_Name:<21}{As_Dollars(Balance_Due):<13}{As_Dollars(Credit_Remain):<10}{As_Dollars(Min_Payment):>11}")
f.close()

# Bottom of the report
print("=" * 64)
print(F" TOTAL CUSTOMER LISTED: {Cus_Count:<3}   {As_Dollars(BalDueAcc):>10}              {As_Dollars(MinPayAcc):>10}")