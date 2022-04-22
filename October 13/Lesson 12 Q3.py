# FileName: Lesson 12 Q3
# Snuggly Company
# Author: Mike Wadden
# Date: October 18, 2021

def Name_Validation(Name):
    """ Function to Validate a Name for Input: Allowing Spaces, - and '"""
    for Char in Name:
        if ("A" <= Char <= "Z" or "a" <= Char <= "z" or Char == " "
                or Char == "-" or Char == "'"):
            continue
        else:
            return False
    return True



PRICE1 = 29.99
PRICE2 = 24.99
PRICE3 = 21.99
SHIPPING_COST1 = 3.99
SHIPPING_COST2 = 5.99
TAX = 0.15
SERVICE_FEE = 0.03


# Province Info

P = {"Newfoundland Labrador: NL", "Prince Edward Island: PE", "Nova Scotia: NS", "New Brunswick: NB",
     "Quebec: QC", "Ontario: ON", "Manitoba: MB", "Saskatchewan: SK", "Alberta: AB",
     "British Columbia: BC", "Yukon: YT", "Northwest Territories: NT", "Nunavut: NU"}

Province_List = ["NL", "PE", "NS", "NB", "QC", "ON", "MB", "SK", "AB", "BC", "YT", "NT", "NU"]

# Inputs

# Customer Name Validation
while True:
    print()
    print("Please Enter Customer Information")
    print()
    print("Enter end for customer name to End program.")
    print()
    while True:

        Customer_Name = input("Enter Your Name: ").title()

        if Customer_Name.upper() == "END":   #Code to End the Program
            break

        elif Customer_Name == "":
            print("Name cannot be blank: Please Re-Enter")

        elif Name_Validation(Customer_Name) == False: #Function to Validate Name I
            print("Invalid Name Entered: Please use letters between (a-z), (-) and (') ")
        else:
            break

    if Customer_Name.upper() == "END":
        print("Good Bye")
        break

    Street_Address = input("Street Address: ")

    while True:
        Province = input("Enter two Digit Province Code: ").upper()
        if Province == " ":
            print("Input Cannot be Blank. Please Re-enter")
        elif len(Province) == 2 and Province in Province_List:
            break
        else:
            print("Invalid Entry: Please Enter two Digit Province Code: ")
            for Code in P:
                print(Code)

    while True:
        City = input("City: ")
        if City == "":
            print("City entry Cannot be Blank. Please Re-enter")
        else:
            break

    while True:
        Postal_Code = input("Postal Code: ").upper().strip()
        if Postal_Code == "":
            print("Postal Code Entry Cannot be Blank. Please Re-enter")

        if (Postal_Code[0].isalpha() == True and Postal_Code[1].isdigit() == True and len(Postal_Code) == 6
                and Postal_Code[2].isalpha() == True and Postal_Code[3].isdigit() == True and Postal_Code[4].isalpha()
                and Postal_Code[5].isdigit() == True):
            break
        else:
            print("Invalid Postal Code: Please Re-Enter (A1A1A1)")

    while True:
        try:
            Phone_Number = int(input("Enter 10 Digit Phone Number: "))
        except:
            print("Invalid Entry!: Enter 10 Digit Phone Number no '-' needed")
        else:
            Phone_Number = str(Phone_Number)
            if len(Phone_Number) == 10:
                break
            else:
                print("Invalid Entry!: Enter 10 Digit Phone Number no '-' needed")

    while True:
        try:
            Credit_Card = int(input("Enter Credit Card Number: "))
        except:
            print("Invalid Entry: Please Enter a Valid Credit Card Number ")
        else:
            Credit_Card = str(Credit_Card)
            if Credit_Card == "":
                print("Invalid Entry: Credit Card Number cannot be blank ")
            elif len(Credit_Card) == 16:
                break
            else:
                print("Invalid Entry Please Enter The 16 digit Credit Card Number. ")

    while True:
        try:
            Order = int(input("Snuggly Order Quantity: "))
        except:
            print("Invalid Order Quantity must be a Interget between 1-20: ")
        else:
            if Order == "":
                print("Order Quantity Cannot be blank: Please try again")
            elif Order <= 0 or Order > 20:
                print("Invalid Entry: Please Enter a order quantity between 1 & 20 ")
            else:
                break

    while True:
        Payment_Method = input(" Enter Payment Method: (C)-CreditCard or (P)-Pay Later: ")
        if Payment_Method == "":
            print("Order Quantity Cannot be blank: Please try again")
        elif Payment_Method.upper() != "C" and Payment_Method.upper() != "P":
            print("Invalid Entry Please enter (C) or (P): ")
        elif Payment_Method.upper() == "C":
            Payment_Method_Dis = "CreditCard Payment"
            break
        elif Payment_Method.upper() == "P":
            Payment_Method_Dis = "Pay Later"
            break

    # Logic Processing

    if Order == 1:
        Price = PRICE1
        Shipping_Cost = SHIPPING_COST2
    elif Order >= 2 and Order <= 5:
        Price = PRICE2
        Shipping_Cost = SHIPPING_COST2
    elif Order >= 6 and Order <= 9:
        Price = PRICE2
        Shipping_Cost = SHIPPING_COST1
    elif Order >= 10:
        Price = PRICE3
        Shipping_Cost = SHIPPING_COST1
    else:
        print("Invalid Entry for Order Input")

    # Calculation Processing

    Order_Cost = Price * Order
    Shipping_Cost_Total = Shipping_Cost * Order
    Subtotal = Order_Cost + Shipping_Cost_Total
    HST = Subtotal * TAX
    Total = Subtotal + HST
    Service_Charge = Total * SERVICE_FEE

    # Formatting for Output
    Order_Cost_Dis = "${:,.2f}".format(Order_Cost)
    Shipping_Cost_Total_Dis = "${:,.2f}".format(Shipping_Cost_Total)
    Subtotal_Dis = "${:,.2f}".format(Subtotal)
    HST_Dis = "${:,.2f}".format(HST)
    Total_Dis = "${:,.2f}".format(Total)
    Service_Charge_Dis = "${:.2f}".format(Service_Charge)
    Order_Dis = "{:,}".format(Order)
    CreditCard_Number_Dis = "{}".format(Credit_Card)
    Price_Dis = "${:,.2f}".format(Price)
    Phone_Number_Dis = f"({Phone_Number[0:3]}) {Phone_Number[3:6]}-{Phone_Number[6:10]}"
    # Output

    Company_Name = "The Snuggly Company"
    print()
    print(Company_Name.center(75))
    print(" " * 26, "Customer Order Forum")
    print()
    print(" " * 2, "{:15} {:<28} {:<20}".format("Customer Name:", Customer_Name.title(), "Credit Card Number: "))
    print(" " * 2, "{:15} {:<28} {:^20}".format(" ", " ", CreditCard_Number_Dis))
    print()
    print(" " * 2, "{:15} {:<28} {:<20}{:<20}".format("Street Adress:", Street_Address, "Order Quantity: ", Order_Dis))
    print(" " * 2, "{:15} {:<28} {:<20}{:<20}".format("Province:", Province, "Snuggly Price:", Price_Dis))
    print(" " * 2, "{:15} {:<28} {:<20}".format("City:", City, "-" * 29))
    print(" " * 2,
          "{:15} {:<28} {:<20}{:<20}".format("Postal Code:", Postal_Code, "Total Snuggly Cost:", Order_Cost_Dis))
    print(" " * 2,
          "{:15} {:<28} {:<20}{:<20}".format("Phone Number:", Phone_Number_Dis, "Shipping Cost:", Shipping_Cost_Total_Dis))
    print(" " * 2, "{:15} {:<28} {:<20}{:<20}".format(" ", " ", "Subtoal", Subtotal_Dis))
    print(" " * 2, "{:15} {:<28} {:<20}{:<20}".format(" ", " ", "Tax:", HST_Dis))
    print(" " * 2, "{:15} {:<28} {:<20}".format(" ", " ", "-" * 29))
    print(" " * 2, "{:15} {:<28} {:<20}{:<20}".format(" ", " ", "Total", Total_Dis))
    print()
    print("*" * 80)
    print()
    print("Payment Method: {}".format(Payment_Method_Dis))
    if Payment_Method.upper() == "C":
        print("Credit Card Service Fee: {}".format(Service_Charge_Dis))
    print()

