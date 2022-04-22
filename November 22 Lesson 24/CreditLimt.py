# FileName: Lesson 26 R1
# ABC Customer Analysis: Credit Limit
# Author: Mike Wadden
# Date: November 25, 2021

def Credit_Limit():
    """Customer Analysis Report: to show customers over there Credit Limit"""
    import datetime


    def As_Dollars(Number):
        """Format Dollars amounts to strings"""
        Number_Display = f"${Number:,.2f}"
        return Number_Display


    def Date_Change(Date):
        """Convert Date input (YYYY-MM_DD) into a datetime object"""
        Date = datetime.datetime.strptime(Date, "%Y-%m-%d")
        return Date


    Today = datetime.datetime.now().date()

    # Title & Headings

    print()
    print("ABC COMPANY")
    print(f"CUSTOMER ANALYSIS AS OF {Today}")
    print()
    print(f"Customer(s) over their credit Limit")
    print()
    print("CUSTOMER    CUSTOMER            PHONE     BALANCE    MINIMUM  DAYS LAST  DAYS LAST")
    print("NUMBER        NAME              NUMBER      DUE      PAYMENT   PURCHASE    PAYMENT      STATUS")
    print("=" * 100)

    # Accumlators set up

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

        Credit_Check = Credit_Limit - Balance_Due

        # Date processing
        Days_Last_Purchase = (Today - Last_Purchase_Date)
        Days_Last_Payment = (Today - Last_Payment_Date)
        Days_Last_Purchase = Days_Last_Purchase
        Pay_Days = Days_Last_Payment.days
        Purch_Days = Days_Last_Purchase.days

        # Processing
        if Balance_Due > Credit_Limit:
            Min_Payment = (Balance_Due * .10) + (Credit_Limit * .10) + (Balance_Due - Credit_Limit)

            # Over Credit Limit Accumulators Processing
            OverLimitAcc += 1
            MinPayAcc += Min_Payment
            CusCount += 1
            BalDueAcc += Balance_Due
            Status = "OVER"

            if Purch_Days > 60:
                Status += "-PURCH"

            if Pay_Days > 30:
                Status += "-Pay"
                # Output
            print(
                f" {Account_Number:5} {Customer_Name:<22}  {Phone_Number[4:12]:<10} {As_Dollars(Balance_Due):<9}  {As_Dollars(Min_Payment):<9}"
                f" {' ' * 2}{Purch_Days:<3} {' ' * 7} {Pay_Days:<3}     {Status:<14}")
        else:
            continue

    if CusCount == 0:
        print("No Entries for Customers over their Creidt Limit")

    print("=" * 100)
    print(f"CUSTOMERS LISTED: {CusCount:3} {' ' * 18} {As_Dollars(BalDueAcc):<10} {As_Dollars(MinPayAcc):<10}")
    print(f"CUSTOMERS OVER LIMIT: {OverLimitAcc}")
    print()
    print()
    AnyKey = input("Press any key to Return to Menu....")
    print()
    f.close()
