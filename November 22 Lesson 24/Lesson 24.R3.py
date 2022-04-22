# FileName: Lesson 24 R3
# customer listings
# Author: Mike Wadden
# Date: November 22, 2021

def As_Dollars(Number):
    """Format Dollars amounts to strings"""
    Number_Display = f"${Number:,.2f}"
    return Number_Display
def Date_Change(Date):
    """Convert Date input (YYYY-MM_DD) into a datetime object"""
    Date = datetime.datetime.strptime(Date, "%Y-%m-%d")
    return Date


import datetime
Today = datetime.datetime.now().date()

# Headings top of the report
print("Widgits Incorporated")
print()
print(f"CUSTOMER LISTING")
print()
print(f"{'CUSTOMER'}{' ' * 5} {' CUSTOMER'}{' ':13}{' ' * 9} {'BALANCE'}{' ' * 5} {'NEXT PAY'}")
print(f"{' NUMBER'}{' ' * 5} {'    NAME'} {' ' * 11} {'PHONE '}{' ' * 5} {'  DUE'}{' ' * 9} {'DAY'}")
print("=" * 68)

# Accumulators

Cus_Count = 0
BalDueAcc = 0


# Report Details
f = open("Customers.dat", "r")
for CustomerData in f:
    CustomerLine = CustomerData.split(",")
    Account_Number = CustomerLine[0]
    Customer_Name = CustomerLine[1].strip()
    Phone_Number = CustomerLine[4].strip()
    Balance_Due = float(CustomerLine[5].strip())
    Next_Pay_Date = Date_Change(CustomerLine[11].strip())
    #Accounmulator Calculations
    Cus_Count += 1
    BalDueAcc += Balance_Due

    print(f"{Account_Number:8} {Customer_Name:<20} {Phone_Number:<16}{As_Dollars(Balance_Due):<11}{Next_Pay_Date.strftime('%b %d, %Y'):>11}")
f.close()

# Bottom of the report
print("=" * 68)
print(F"TOTAL CUSTOMER LISTED: {Cus_Count:<2}{' ' *21}{As_Dollars(BalDueAcc):<10}")