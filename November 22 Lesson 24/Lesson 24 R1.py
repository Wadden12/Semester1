# FileName: Lesson 24
# Accounts Receivable Customer Listings
# Author: Mike Wadden
# Date: November 22, 2021

# Headings top of the report
print(f"{' '* 22}{'WIDGITS INCORPORATED'}")
print()
print(f"{' ' *13}{'ACCOUNTS RECEIVABLE CUSTOMER LISTING'}")
print()
print(f"{' ' *11}{'ACCOUNT':18}{'CUSTOMER':18} {'PHONE':>10}")
print(f"{' ' *11}{'NUMBER':18}{'   NAME':18}  {'NUMBER':>10}")
print(" " * 10, "=" * 51)

Cus_Count = 0
# Report Details
f = open("Customers.dat", "r")
for CustomerData in f:
    CustomerLine = CustomerData.split(",")
    Account_Number = CustomerLine[0]
    Customer_Name = CustomerLine[1].strip()
    Phone_Number = CustomerLine[4].strip()
    print(f"{' ' *11}{Account_Number:5}        {Customer_Name:25}{Phone_Number}")
    Cus_Count += 1
f.close()

# Bottom of the report
print(" " * 10,"=" * 51)
print(F" {' ' *10} TOTAL CUSTOMER LISTED: {Cus_Count}")





