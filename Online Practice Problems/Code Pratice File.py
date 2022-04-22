# FileName: Lesson 16 Q1
# Hotel Problem (Test Version)
# Author: Mike Wadden
# Date: October 21, 2021

import datetime

# Constants

REG_RATE = 85
SUMMER_RATE = 105  # for Months of July and August

Continue = "N"

while Continue != "Y":
    # inputs

    while True:
        try:
            print()
            Arrival_Date = input("Enter Start Date: using (YYYY-MM-DD) format ")
            Arrival = datetime.datetime.strptime(Arrival_Date, "%Y-%m-%d").date()
            Departure_Date = input("Enter End Date: using (YYYY-MM-DD))  format ")
            Depart = datetime.datetime.strptime(Departure_Date, "%Y-%m-%d").date()
        except:
            print("Invalid Date Entry. Re-Enter using (YYYY-MM-DD))")
        else:
            if Depart < Arrival:
                print("Invalid Entry: End Date Cannot be before Start Date: ")
            else:
                break

    Arrival_Out = Arrival   #Used for output since Arrival is modified in lower calculations

    # Output Message Check

    if (Arrival.month < 7 and Depart.month < 7) or (Arrival.month > 8 and Depart.month > 8):
        Rate_Message = ""
    elif Arrival.month < 7 and Depart.month <= 8:
        Rate_Message = "(Mixed Rate)"
    elif Arrival.month >= 7 and Depart.month <= 8:
        Rate_Message = "(High Season Rate Applied)"
    elif Arrival.month >= 7 and Depart.month > 8:
        Rate_Message = "(Mixed Rate)"

    # loop to charge the rate per day

    Delta = datetime.timedelta(days=1)
    Total_Nights = (Depart - Arrival).days
    Total_Price = 0
    n = 0

    while n != Total_Nights:      # Loop is set by the number of nights stayed
        if Arrival.month == 7 or Arrival.month == 8:
            Nightly_Rate = SUMMER_RATE
        else:
            Nightly_Rate = REG_RATE

        Total_Price += Nightly_Rate
        Arrival += Delta      # looks at individual days so the daily rate can be applied
        n += 1     # Counter for the to break loop

    Nightly_Average = Total_Price / Total_Nights  # Works out new Nightly Rate when mixed

    # Output

    print()
    print("The Hotel Reservation Program")
    print()
    print(f"Arrival Date:   {Arrival_Out.strftime('%B %d, %Y')}")
    print(f"Departure Date: {Depart.strftime('%B %d, %Y')}")
    print(f"Nightly Rate:   ${Nightly_Average:,.2f}{Rate_Message}")
    print(f"Total Nights:   {Total_Nights}")
    print(f"Total Price:    ${Total_Price:,.2f}")

    # This code prompts the user if they want to make another entry

    print()

    while Continue.upper() == "Y" or "N":
        Continue = input("Do you want to make another Entry? (Y) or (N) ")
        if Continue.upper() == "Y":
            break
        elif Continue.upper() == "N":
            print()
            print("Thank You for using The Hotel Reservation Program. Bye Bye")
            break
        else:
            print("Incorrect Value entered, Please Enter Y or N")

    if Continue.upper() == "N":
        break

