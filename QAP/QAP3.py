# FileName: QAP3
# Honest Harry Car Sales (Looking for a program to keep track of his sales)
# Author: Mike Wadden
# Date: October 27, 2021

# imports
import datetime

# Constants

TAX_RATE = .15
STAND_FEE = 75         #Lincence Fee for vechiles  <= $5,000
LUX_FEE = 165          #Lincence Fee for Vechiles >$5,000
TRANS_RATE = 0.01      #transfer Fee 1%
LUX_RATE = 0.016       # Lux Tax on Vechilces > $20,000
MIN_CAR_DATE = "2010"  # Set the oldest Model of Car's sold by the company:
#Functions

def As_Dollars(Number):
    """Format Dollars amounts to strings"""
    Number_Display = f"${Number:,.2f}"
    return Number_Display


def Name_Validation(Name):
    """ Function to Validate a Name for Input: Allowing Spaces, - and '"""
    for Char in Name:
        if ("A" <= Char <= "Z" or "a" <= Char <= "z" or Char == " "
                or Char == "-" or Char == "'"):
            continue
        else:
            return False
    return True

def Time_Change(Date):
    """Convert Date input (YYYY-MM_DD) into a datetime object"""
    import datetime
    Date = datetime.datetime.strptime(Date, "%Y-%m-%d")
    return Date

# Province Info

P = {"Newfoundland Labrador: NL", "Prince Edward Island: PE", "Nova Scotia: NS", "New Brunswick: NB",
     "Quebec: QC", "Ontario: ON", "Manitoba: MB", "Saskatchewan: SK", "Alberta: AB",
     "British Columbia: BC", "Yukon: YT", "Northwest Territories: NT", "Nunavut: NU"}

Province_List = ["NL", "PE", "NS", "NB", "QC", "ON", "MB", "SK", "AB", "BC", "YT", "NT", "NU"]

MIN_CAR_DATE = datetime.datetime.strptime(MIN_CAR_DATE, "%Y")            #Oldest Car still in operation for a extra Validation
Today_Date = datetime.datetime.now()
Max_Date = Today_Date + datetime.timedelta(days=365)             #Calculate the Max Date for cars that could be sold

# Inputs
# Customer Details Inputs

while True:
    print()
    print("Please Enter Customer Information")
    print()
    print("Enter (END) for Customer First Name to Exit Program.")
    print()

    while True:
        Cus_First_Name = input("First Name: ").title().lstrip().rstrip()
        if Cus_First_Name.upper() == "END":                                         #Code to End the Program
            break
        elif Cus_First_Name == "":
            print("First Name cannot be blank: Please Re-Enter")
        elif len(Cus_First_Name) >25:
            print("Invalid First Name Length: Cannot be longer than 25 letters ")
        elif Name_Validation(Cus_First_Name) == False:                              #Function to Validate Name Input
            print("Invalid Name Entered: Please use letters between (a-z), (-) and (') ")
        else:
            break

    if Cus_First_Name.upper() == "END":
        print()
        print("Good Bye")
        print()
        break

    while True:
        Cus_Last_Name = input("Last Name: ").title().lstrip().rstrip()
        if Cus_Last_Name == "":
            print("Last Name cannot be blank: Please Re-Enter")
        elif len(Cus_Last_Name) > 30:
            print("Invalid Last Name Length: Cannot be longer than 30 letters ")
        elif Name_Validation(Cus_Last_Name) == False:                               #Function to Validate Name Input
            print("Invalid Name Entered: Please use letters between (a-z), (-) and (') ")
        else:
            break

    while True:
        Street_Address = input("Street Address: ").lstrip().rstrip().title()
        if Street_Address == "":
            print("Street Address Input cannot be blank: ")
        elif len(Street_Address) > 35:
            print("Invalid Entry Street Address Length: Cannot be longer than 35 characters ")
        else:
            break

    while True:
        City = input("City: ").lstrip().rstrip()
        if City == "":
            print("City Input cannot be blank: ")
        elif len(City) > 20:
            print("Invalid Entry City Length: Cannot be longer than 20 characters ")
        else:
            break

    while True:
        Province = input("Enter two Digit Province Code: ").upper()
        if Province in Province_List:
            break
        else:
            print()
            print("Invalid Entry: Please Enter two Digit Province Code: ")
            print()
            for Code in P:
                print(Code)

    while True:
        Postal_Code = input("Postal Code: ").upper().strip()
        if Postal_Code == "":
            print("Postal Code Entry Cannot be Blank. Please Re-enter")
        elif (Postal_Code[0].isalpha() == True and Postal_Code[1].isdigit() == True and len(Postal_Code) == 6
                and Postal_Code[2].isalpha() == True and Postal_Code[3].isdigit() == True and Postal_Code[4].isalpha()
                and Postal_Code[5].isdigit() == True):
            break
        else:
            print("Invalid Postal Code: Please Re-Enter (A1A1A1)")

    while True:
        Phone_Number = input("Enter 10 Digit Phone Number: ").strip().replace("-", "")
        if Phone_Number.isdigit() == False:
            print("Invalid Entry!: Enter 10 Digit Phone Number no '-' needed")
        elif len(Phone_Number) != 10:
            print("Invalid Entry!: Enter 10 Digit Phone Number no '-' needed")
        else:
            break

    while True:  # Date Validation Loop
        try:
            Purchase_date = input("Enter Invoice Date as (YYYY-MM-DD): ")
            Purchase_date = Time_Change(Purchase_date)
        except:
            print("Invalid Date Entry. Re-Enter using (YYYY-MM-DD)")
        else:
            if Purchase_date > datetime.datetime.now():
                print("Invalid Date: Cannot future Date Purchases ")
            else:
                break

    print()
    print("Enter Car Details")           #Car Details Inputs
    print()

    while True:
        Plate_Number = input("Licence Plate Number format XXX999: ").strip().upper()
        if Plate_Number == "":
            print("Licence Plate Entry Cannot be Blank. Please Re-enter")
        elif Plate_Number[0:3].isalpha() == False or Plate_Number[3:6].isdigit() == False:  #Licence Plate Validation for the correct format
            print("Invalid Entry: Ensure entry has 3 letters and 3 digits ie: (AAA999) ")
        else:
            break

    while True:
        Car_Make = input("Enter the Car's Make & Model: ").title().lstrip().rstrip()
        if Car_Make == "":
            print("Car Make & Model: Entry Cannot be Blank. Please Re-enter")
        else:
            break

    while True:
        try:
            print()
            print(F"The Min Year: {MIN_CAR_DATE.year} & Max Year {Max_Date.year}")
            print("For Special Entries outside this range input (S) for Car Year")
            print()

            Car_Year = input("The Year of the Car: YYYY: ").lstrip().rstrip()

            # This allow for a special input outside of min-max range
            if Car_Year.upper() == "S":
                print()
                Car_Year = input("Special Request input for car Year: YYYY ").lstrip().rstrip()
                Car_Year = datetime.datetime.strptime(Car_Year, "%Y")
                Car_Year = str(Car_Year.year)
                break
            Car_Year = datetime.datetime.strptime(Car_Year, "%Y")
        except:
            print("Invalid Car Year Entry: Input as per example: 2021 ")
        else:
            if Car_Year > Max_Date:
                print(f"Invalid Entry: Car Year cannot be greater than '{Max_Date.year}' ")
            elif Car_Year < MIN_CAR_DATE:
                print(f"Invalid Entry: The oldest Model is set to '{MIN_CAR_DATE}' ")
            else:
                Car_Year = str(Car_Year.year)
                break

    while True: #Validation Loop for Selling and Trade Allowance
        try:
            Sell_Price = float(input("Sell Price: $").lstrip().rstrip())
            Trade_Price = float(input("Trade Allowance: $").lstrip().rstrip())
        except:
            print("Invalid Entry:Input the Selling Price: ")
        else:
            if Sell_Price > 50000:
                print()
                print("Invalid Entry: Selling Price cannot exceed $50,000")
                print()
            elif Sell_Price < 0:
                print()
                print("Invalid Entry: Selling Price cannot be less than 0 ")
                print()
            elif Trade_Price > Sell_Price:
                print()
                print("Invalid Entry: Trade Allowance cannot be higher than Selling Price ")
                print()
            else:
                break

    while True:
        Sales_Rep = input("Enter Sales Rep Name: ").title().lstrip().rstrip()
        if Sales_Rep == "":
            print("Name cannot be blank: Please Re-Enter")

        elif Name_Validation(Sales_Rep) == False: #Function to Validate Name I
            print("Invalid Name Entered: Please use letters between (a-z), (-) and (') ")
        else:
            break

    while True:
        try:
            Credit_Card = int(input("Enter Credit Card Number: ").strip())
        except:
            print("Invalid Entry: Please Enter a Valid Credit Card Number ")
        else:
            Credit_Card = str(Credit_Card)
            if Credit_Card == "":
                print("Invalid Entry: Credit Card Number cannot be blank ")
            elif len(Credit_Card) == 16:
                Credit_Card = f"{Credit_Card[0:4]} {Credit_Card[4:8]} {Credit_Card[8:12]} {Credit_Card[12:16]}"
                break
            else:
                print("Invalid Entry Please Enter The 16 digit Credit Card Number. ")

    while True:
        try:
            Expiry_Date = input("Credit Card Expiry date: MM/YY ")
            Expiry_Date = datetime.datetime.strptime(Expiry_Date, "%m/%y")
        except:
            print("Invalid Date Entry. Re-Enter using (MM/YY)")
        else:
            break

    # Processing

    After_TradeP = Sell_Price - Trade_Price
    Hst = Sell_Price * TAX_RATE
    Transfer = Sell_Price * TRANS_RATE

    # Logic Statements for Lincense Fee and Lux Tax

    if Sell_Price <= 5000:
        Lincense_Fee = STAND_FEE
        Lux_Tax = 0
    elif Sell_Price > 5000 and Sell_Price <= 20000:
        Lincense_Fee = LUX_FEE
        Lux_Tax = 0
    else:
        Lincense_Fee = LUX_FEE + (Sell_Price * LUX_RATE)

    Total_Price = After_TradeP + Hst + Transfer + Lincense_Fee

    #  For Loop For Monthly Payment Display
    print()
    AnyKey = input("Press any key to Display Financing Options....")
    print()
    print("# Years   # Payments   Financing Fee   Total Price  Monthly Payment")

    for Years in range(1, 5) :    #Loop to show  different monthly payments for the customer to choose

        New_Price = Total_Price
        Payment = 12 * Years
        Financing_Fee = 39.99 * Years   #Financing Fee $39.99
        New_Price += Financing_Fee
        Monthly_Payment = New_Price / Payment

        print(F"    {Years:1}          {Payment:2}       {As_Dollars(Financing_Fee):>10}      {As_Dollars(New_Price):10}      {As_Dollars(Monthly_Payment):>10}")

    print()

    while True:
        try:
            Pay_Plan = int(input("Enter the payment schedule you want to follow (1-4): #"))
        except:
            print("Invlaid Entry: Please Enter a number Between 1-4 ")
        else:
            if Pay_Plan < 1 or Pay_Plan > 4:
                print("Invalid Entry Select a payment schedule between (1-4 ")
            else:
                break

    # Monthly Payment Processing

    Payment = 12 * Pay_Plan
    Financing_Fee = 39.99 * Pay_Plan
    Total_Price += Financing_Fee
    Monthly_Payment = Total_Price / Payment
    First_Payment = Purchase_date + datetime.timedelta(days=30)  # First Payment

    #Receipt ID

    Receipt_ID = f"{Cus_First_Name[0]}{Cus_Last_Name[0]}-{Plate_Number[3:6]}-{Phone_Number[6:10]}"

    #Outputs

    print()
    print(" " * 6, "Honest Harry Car Sales")
    print(" " * 5, "Used Car Sale and Receipt")
    print()
    print(f"Invoice Date: {Purchase_date.strftime('%b %d, %Y')}")
    print(f"Receipt No: {Receipt_ID}")
    print()
    print("Sold to:")
    print(f"{' ' * 5}{Cus_First_Name[0]}.{Cus_Last_Name}")
    print(f"{' ' * 5}{Street_Address}")
    print(f"{' ' * 5}{City},{Province:2},{Postal_Code}")     #Added a max length for the city in validation to be 25 chars to keep format
    print()
    print("Car Details:")
    print(f"{' ' * 5}{Car_Year} {Car_Make}")
    print()
    print(f"{'Sale price:':25}{As_Dollars(Sell_Price):>10}")
    print(f"{'Trade Allowance:':25}{As_Dollars(Trade_Price):>10}")
    print(f"{'Price after Trade:':25}{As_Dollars(After_TradeP):>10}")
    print(f"{' ':25}{'-' * 10}")
    print(f"{'HST:':25}{As_Dollars(Hst):>10}")
    print(f"{'License Fee:':25}{As_Dollars(Lincense_Fee):>10}")
    print(f"{'Transfer Fee:':25}{As_Dollars(Transfer):>10}")
    print(f"{' ':25}{'-' * 10}")
    print(f"{'Total Sales Cost: ':25}{As_Dollars(Total_Price):>10}")
    print()
    print(f"Terms: {Pay_Plan}{' '* 9}{'Total payments:'} {Payment}")
    print(f"{'Monthly payment':25}{As_Dollars(Monthly_Payment):>10}")
    print()
    print(" " * 3, "Honest Harry Car Sales")
    print("Best used cars at the best price!")
    print()

    # This code prompts the user if they want to make another entry(Secondary Exit Point for the user)
    while True:
        Continue = input("Do you want to make another Entry?  (Y) or (N) ")
        if Continue.upper() == "Y":
            break
        elif Continue.upper() == "N":
            print()
            Cus_First_Name = "END"
            break
        else:
            print("Incorrect Value entered, Please Enter Y or N")

    if Cus_First_Name == "END":
        print()
        print("Good Bye")
        print()
        break