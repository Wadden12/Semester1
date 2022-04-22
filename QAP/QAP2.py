# FileName: QAP2
# St.John's Marina & Yacht Club: Looking for a program to create digital Receipts for Members
# Author: Mike Wadden
# Date: September 27,2021

import datetime

# Constants

EVEN = 80  # Cost of Even number sites
ODD = 120  # Cost of Odd Sites
ALTMEMBER_COST = 5  # Cost per person for family and friends allowed to visit the site
CLEANING_COST = 50
VIDEO_COST = 35  # Video Surveillance Cost
TAX = 0.15
STANDARD = 75  # Standard Membership
EXECUTIVE = 150  # Executive Membership
PROCESSING_FEE = 59.99
CANCEL_RATE = .60
COMPANY_NAME = "St.John's Marina & Yacht Club"

# Province Info

P = {"Newfoundland Labrador: NL", "Prince Edward Island: PE", "Nova Scotia: NS", "New Brunswick: NB",
     "Quebec: QC", "Ontario: ON", "Manitoba: MB", "Saskatchewan: SK", "Alberta: AB",
     "British Columbia: BC", "Yukon: YT", "Northwest Territories: NT", "Nunavut: NU"}

Province_List = ["NL", "PE", "NS", "NB", "QC", "ON", "MB", "SK", "AB", "BC", "YT", "NT", "NU"]

# User Inputs and some validation


Continue = "N"
while Continue != "Y":
    while True:  # Checks to ensure a valid site number is input
        Site_Number = int(input("Enter Site Number from 1 to 100 # "))
        if Site_Number >= 1 and Site_Number <= 100:
            break
        else:
            print("Invalid Entry: Enter a Number from 1 to 100")

    Member_Name = input("Member Name: ").title()
    Street_Address = input("Street Address: ")
    City = input("City: ")

    while True:
        Province = input("Enter two Digit Province Code: ").upper()
        if len(Province) == 2 and Province in Province_List:
            break
        else:
            print("Invalid Entry: Please Enter two Digit Province Code: ")
            for Code in P:
                print(Code)

    while True:
        Postal_Code = input("Postal Code: ").upper()
        if len(Postal_Code) == 6:
            break
        else:
            print("Invalid Entry! Please Enter a 6 Digit Postal Code")

    while True:
        Phone_Number = input("Enter 10 Digit Phone Number: ")
        if len(Phone_Number) == 10:
            break
        else:
            print("Invalid Entry!: Enter 10 Digit Phone Number no '-' needed")

    while True:
        Cell_Number = input("Enter 10 Digit Cell Number: ")
        if len(Cell_Number) == 10:
            break
        else:
            print("Invalid Entry!: Enter 10 Digit Cell Number no '-' needed")

    while True:
        Membership_Type = input(" Enter Membership Type (S)-Standard or (E)-Executive: ")
        if Membership_Type.upper() == "S":
            Membership_Due = STANDARD
            Membership_Out = "Standard"
            break
        elif Membership_Type.upper() == "E":
            Membership_Due = EXECUTIVE
            Membership_Out = "Executive"
            break
        else:
            print("Invalid Entry! Please Enter (S) or (E) ")

    print("Alternate Member is Family & Friends who be Allowed Access to the Grounds")
    AltMember = int(input("Number of Alternate Members: "))

    while True:
        Cleaning = input("Weekly Site Cleaning (Y)es (N)o :")
        if Cleaning.upper() == "Y":
            Cleaning_Fee = CLEANING_COST
            Cleaning_out = "Yes"
            break
        elif Cleaning.upper() == "N":
            Cleaning_Fee = 0
            Cleaning_out = "No"
            break
        else:
            print("Invalid Entry! Please Enter (Y) or (N) ")

    while True:
        Video = input("Video Surveillance (Y)es or (N)o :")
        if Video.upper() == "Y":
            Video_Fee = VIDEO_COST
            Video_Out = "Yes"
            break
        elif Video.upper() == "N":
            Video_Fee = 0
            Video_Out = "No"
            break
        else:
            print("Invalid Entry! Please Enter (Y) or (N) ")

    # Processing Calculations # Monthly Charges

    if Site_Number % 2 == 0:
        Site_Cost = EVEN
    else:
        Site_Cost = ODD

    AltMember_Total = AltMember * ALTMEMBER_COST

    Site_Total = Site_Cost + AltMember_Total
    Extra_Charge = Cleaning_Fee + Video_Fee

    Subtotal = Site_Total + Extra_Charge
    Sales_Tax = Subtotal * TAX

    Monthly_Charge = Subtotal + Sales_Tax
    Total_Monthly = Monthly_Charge + Membership_Due

    Yearly_Fee = Total_Monthly * 12
    Monthly_Payment = (Yearly_Fee + PROCESSING_FEE) / 12

    Yearly_Site = Site_Total * 12
    Cancel_Fee = Yearly_Site * CANCEL_RATE

    # Format OutPut's

    Site_Total_Dis = "${:,.2f}".format(Site_Total)
    Extra_Charge_Dis = "${:,.2f}".format(Extra_Charge)
    Subtotal_Dis = "${:,.2f}".format(Subtotal)
    Sales_Tax_Dis = "${:,.2f}".format(Sales_Tax)
    Monthly_Charge_Dis = "${:,.2f}".format(Monthly_Charge)
    Total_Monthly_Dis = "${:,.2f}".format(Total_Monthly)
    Membership_Due_Dis = "${:,.2f}".format(Membership_Due)
    Yearly_Fee_Dis = "${:,.2f}".format(Yearly_Fee)
    Monthly_Payment_Dis = "${:,.2f}".format(Monthly_Payment)
    Cancel_Fee_Dis = "${:,.2f}".format(Cancel_Fee)
    Phone_Number_Dis = "{}-{}-{}".format(Phone_Number[:3], Phone_Number[3:6], Phone_Number[6:])
    Cell_Number_Dis = "{}-{}-{}".format(Cell_Number[:3], Cell_Number[3:6], Cell_Number[6:])

    # Date Input
    Date = datetime.datetime.now().date()

    # Output

    print()
    print(" " * 6, COMPANY_NAME)
    print(" " * 10, "Yearly Member Receipt")
    print()
    print(" " * 1, "_" * 35)
    print()
    print(" " * 1, "Client Name and Address:")
    print(" " * 1, Member_Name)
    print(" " * 1, Street_Address)
    print(" " * 1, "{}, {} {}".format(City, Province, Postal_Code))
    print()
    print(" " * 1, "{:6}{}(H)".format("Phone:", Phone_Number_Dis))
    print(" " * 1, "{:6}{}(C)".format(" ", Cell_Number_Dis))
    print()
    print(" " * 1, "Site#: {:<3d} Member type: {}".format(Site_Number, Membership_Out))
    print()
    print(" " * 1, "{:27}{:5}{:>3}".format("Alternate members:", " ", AltMember))
    print(" " * 1, "{:27}{:5}{:>3}".format("Weekly site cleaning:", " ", Cleaning_out))
    print(" " * 1, "{:27}{:5}{:>3}".format("Video Surveillance:", " ", Video_Out))
    print()
    print(" " * 1, "{:24}{:>11}".format("Site charges:", Site_Total_Dis))
    print(" " * 1, "{:24}{:>11}".format("Extra charges:", Extra_Charge_Dis))
    print(" " * 1, "{:24}{:>11}".format("", "-" * 9))
    print(" " * 1, "{:24}{:>11}".format("Subtotal:", Subtotal_Dis))
    print(" " * 1, "{:24}{:>11}".format("Sales tax (HST):", Sales_Tax_Dis))
    print(" " * 1, "{:24}{:>11}".format("", "-" * 9))
    print(" " * 1, "{:24}{:>11}".format("Total monthly charges:", Monthly_Charge_Dis))
    print(" " * 1, "{:24}{:>11}".format("Monthly dues:", Membership_Due_Dis))
    print(" " * 1, "{:24}{:>11}".format("", "-" * 9))
    print(" " * 1, "{:24}{:>11}".format("Total monthly fees:", Total_Monthly_Dis))
    print(" " * 1, "{:24}{:>11}".format("Total yearly fees:", Yearly_Fee_Dis))
    print()
    print(" " * 1, "{:24}{:>11}".format("Monthly payment:", Monthly_Payment_Dis))
    print()
    print(" " * 1, "_" * 35)
    print()
    print(" " * 1, "Issued: ", Date)
    print(" " * 1, "HST Reg No: 549-33-5849-4720-9885")
    print()
    print(" " * 1, "{:24}{:>11}".format("Cancellation fee:", Cancel_Fee_Dis))
    print()
    print("*" * 45)
    # This code prompts the user if they want to make another entry
    while Continue.upper() == "Y" or "N":
        Continue = input("Do you want to make another Entry? (Y) or (N) ")
        if Continue.upper() == "Y":
            break
        elif Continue.upper() == "N":
            print()
            print("Have a Good Day")
            break
        else:
            print("Incorrect Value entered, Please Enter Y or N")

    if Continue.upper() == "N":
        break
