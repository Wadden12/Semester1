# FileName: Lesson 26 R1
# ABC Customer Analysis
# Author: Mike Wadden
# Date: November 25, 2021

def Provice_Match():
    """ Displays Customers from a certain Province based on a user input"""
    import datetime


    def As_Dollars(Number):
        """Format Dollars amounts to strings"""
        Number_Display = f"${Number:,.2f}"
        return Number_Display

    def Date_Change(Date):
        """Convert Date input (YYYY-MM_DD) into a datetime object"""
        Date = datetime.datetime.strptime(Date, "%Y-%m-%d")
        return Date

    P = {"Newfoundland Labrador: NL", "Prince Edward Island: PE", "Nova Scotia: NS", "New Brunswick: NB",
         "Quebec: QC", "Ontario: ON", "Manitoba: MB", "Saskatchewan: SK", "Alberta: AB",
         "British Columbia: BC", "Yukon: YT", "Northwest Territories: NT", "Nunavut: NU"}

    Province_List = ["NL", "PE", "NS", "NB", "QC", "ON", "MB", "SK", "AB", "BC", "YT", "NT", "NU"]

    Today = datetime.datetime.now().date()
    print()
    print("Enter a Province to view customer list from area")
    print()

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

    # Title & Headings
    print()
    print("ABC COMPANY")
    print(f"CUSTOMER ANALYSIS AS OF {Today}")
    print()
    print(f"CUSTOMER ANALYSIS: For Customer from {Province}")
    print()
    print("CUSTOMER    CUSTOMER            PHONE     BALANCE    MINIMUM  DAYS LAST  DAYS LAST")
    print("NUMBER        NAME              NUMBER      DUE      PAYMENT   PURCHASE    PAYMENT      STATUS")
    print("=" * 100)

    #Accumlators set up

    CusCount = 0
    MinPayAcc = 0
    BalDueAcc = 0
    OverLimitAcc = 0

    # Report Details
    f = open("Customers.dat", "r")
    for CustomerData in f:
        CustomerLine = CustomerData.split(",")
        Account_Number = CustomerLine[0]
        Customer_Name = CustomerLine[1].strip()
        Phone_Number = CustomerLine[4].strip()
        Credit_Limit = float(CustomerLine[6].strip())
        Balance_Due = float(CustomerLine[5].strip())
        Last_Purchase_Date = Date_Change(CustomerLine[7].strip()).date()
        Last_Payment_Date = Date_Change(CustomerLine[9].strip()).date()
        ProvMatch = CustomerLine[12].strip()
        Credit_Check = Credit_Limit - Balance_Due

        if Province == ProvMatch:
            # Processing
            if Balance_Due > Credit_Limit:
                Min_Payment = (Balance_Due * .10) + (Credit_Limit * .10) + (Balance_Due - Credit_Limit)
                # Over Credit Limit Accumulators Processing
                OverLimitAcc += 1
                MinPayAcc += Min_Payment
                Status = "OVER"
            else:
                Min_Payment = Balance_Due * .10
                MinPayAcc += Min_Payment
                Status = "OK"
                if Credit_Check <= 200:  # Checks for customers within $200 of there credit limit
                    Status = "CHECK"

             # Date processing
            Days_Last_Purchase = (Today - Last_Purchase_Date)
            Days_Last_Payment = (Today - Last_Payment_Date)
            Days_Last_Purchase = Days_Last_Purchase
            Pay_Days = Days_Last_Payment.days
            Purch_Days = Days_Last_Purchase.days

            if Purch_Days > 60:
                Status += "-PURCH"

            if Pay_Days > 30:
                Status += "-Pay"
            CusCount += 1
            BalDueAcc += Balance_Due
            # Output
            print(f" {Account_Number:5} {Customer_Name:<22}  {Phone_Number[4:12]:<10} {As_Dollars(Balance_Due):<9}  {As_Dollars(Min_Payment):<9}"
                  f" {' '* 2}{Purch_Days:<3} {' '* 7} {Pay_Days:<3}     {Status:<14}")

    if CusCount == 0:
        print(f"No Entries for Customer from {Province}")

    print("=" * 100)
    print(f"CUSTOMERS LISTED: {CusCount:3} {' ' * 18} {As_Dollars(BalDueAcc):<10} {As_Dollars(MinPayAcc):<10}")
    print(f"CUSTOMERS OVER LIMIT: {OverLimitAcc}")
    print()
    print()
    AnyKey = input("Press any key to Return to Menu....")
    print()

    f.close()