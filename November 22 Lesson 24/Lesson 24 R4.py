# FileName: Lesson 24 R4
# Over Credit Limit Report
# Author: Mike Wadden
# Date: November 22, 2021

def As_Dollars(Number):
    """Format Dollars amounts to strings"""
    Number_Display = f"${Number:,.2f}"
    return Number_Display
def Date_Change(Date):
    """Convert Date input (YYYY-MM_DD) into a datetime object"""
    import datetime
    Date = datetime.datetime.strptime(Date, "%Y-%m-%d")
    return Date


import datetime
Today = datetime.datetime.now().date()

# Headings top of the report
print()
print("Widgits Incorporated")
print()
print(f"OVER LIMIT REPORT AS OF {Today}")
print()
print(f"{'CUSTOMER':12}{' CUSTOMER':19}  {'PHONE':10} {'CREDIT':9}{' AMOUNT':9} {'  NEXT':11} {'  PAYMENT':10}")
print(f"{' NUMBER':12}{'   NAME':19}  {'NUMBER':10} {'LIMIT':9}{'  OVER':9} {'PAY DATE':11} {'    DUE':10}")
print("=" * 86)

# Accumulators

Cus_Count = 0
PaymentAcc = 0

# Report Details
f = open("Customers.dat", "r")
for CustomerData in f:
    CustomerLine = CustomerData.split(",")
    Account_Number = CustomerLine[0]
    Customer_Name = CustomerLine[1].strip()
    Phone_Number = CustomerLine[4].strip()
    Credit_Limit = float(CustomerLine[6].strip())
    Balance_Due = float(CustomerLine[5].strip())
    Next_Pay_Date = Date_Change(CustomerLine[11].strip())

    # Processing
    Amount_Over = Credit_Limit - Balance_Due

    if Amount_Over < 0:
        #Accumulators go inside the if because we only want to count those with negative credit
        Payment_Due = (Credit_Limit * .10) + (Amount_Over * -1)
        PaymentAcc += Payment_Due
        Cus_Count += 1
        Amount_Over_Dis = Amount_Over * -1
        print(f"{Account_Number:5} {Customer_Name:<20}  {Phone_Number:<12}  {As_Dollars(Credit_Limit):<9} {As_Dollars(Amount_Over_Dis):<10} {Next_Pay_Date.strftime('%Y %m, %d'):12} {As_Dollars(Payment_Due):>10}")
    else:
        continue

f.close()

# Bottom of the report
print("=" * 86)
print(F"Total customers over limit: {Cus_Count:<2}{As_Dollars(PaymentAcc):>56}")