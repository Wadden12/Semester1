# FileName: Lesson 21 Q1
# Billy Bob Bike Rentals
# Author: Mike Wadden
# Date: November 3, 2021

# Open Default File and read values into Variables
f = open('InvNum.txt', 'r')
InvNum = int(f.readline())
f.close()

def Write(Variable, f):
    """Function to Convert None Strings to Strings and Format to write to file with ,"""
    import datetime
    if isinstance(Variable, str) == False:
        if isinstance(Variable, datetime.datetime) == True:
            return f.write(f"{Variable.strftime('%Y-%m-%d')}, ")
        else:
            return f.write(f"{str(Variable)}, ")
    elif isinstance(Variable, str) == True:
        return f.write(f"{(Variable)}, ")


def Write_Space(Variable, f):
    """Function to Convert None Strings to Strings and Format to write to file with Space"""
    import datetime
    if isinstance(Variable, str) == False:
        if isinstance(Variable, datetime.datetime) == True:
            return f.write(f"{Variable.strftime('%Y-%m-%d')}\n")
        else:
            return f.write(f"{str(Variable)}\n")
    elif isinstance(Variable, str) == True:
        return f.write(f"{(Variable)}\n")

# Continue Loop

Continue = "N"
while Continue != "Y":

    # Input and Valadation
    while True:
        Customer_Name = input("Enter Customer Name: ")
        if Customer_Name == "":
            print("Invalid Entry: Customer Name can not be blank ")
        else:
            break

    while True:
        Phone_Number = input("Enter 10 Digit Phone Number: ")
        if len(Phone_Number) == 10:
            break
        else:
            print("Invalid Entry!: Enter 10 Digit Phone Number no '-' needed")

    while True:
        Bike_Code = input("Enter Bike Code: (T)-12 Speed, (M)- Mountain Bike or (B)-Bicycle Built for 2: ")
        if Bike_Code == "":
            print("Invalid Entry: Bike Code Cannot be blank: Re-Enter (T), (M) or (B)")
        elif Bike_Code.upper() != "T" and Bike_Code.upper() != "B" and Bike_Code.upper() != "M":
            print("Invalid Entry: Please Enter (T)-12 Speed, (M)-Mountain Bike or (B)-Bicycle Built for 2")
        else:
            break

    while True:
        try:
            Rent_Bikes = int(input("Enter Number of Bikes Rented between 1-3: "))
        except:
            print("Rented Bikes is not a Valid Entry: Please Re-Enter.")
        else:
            if Rent_Bikes < 1 or Rent_Bikes > 3:
                print("Invalid Entry: Please Enter a Number Between 1 & 3 ")
            else:
                break

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

    #Output Processing
    print("Invoice Number: ", InvNum)
    print("Customer Name: ", Customer_Name)
    print("Phone Number", Phone_Number)
    print("Bike Code", Bike_Code)
    print("Rented Bikes: ", Rent_Bikes)

    #Writing File to Rentals.dat
    f = open('Rentals.dat', 'a')
    Write(InvNum, f)
    Write(Customer_Name, f)
    Write(Phone_Number, f)
    Write(Bike_Code, f)
    Write_Space(Rent_Bikes, f)
    f.close()

    InvNum += 1  # Updates the Invoice Number
    f = open('InvNum.txt', 'w')
    Write_Space(InvNum, f)
    f.close()
#Program Continue Question

    while Continue.upper() == "Y" or "N":
        Continue = input("Do you want to make another Entry? (Y) or (N) ")

        if Continue == "":
            print("Continue Cannot be Blank: Please Re-enter:")
        elif Continue.upper() == "Y":
            break
        elif Continue.upper() == "N":
            print()
            print("Have a Good Day")
            break
        else:
            print("Incorrect Value entered, Please Enter Y or N")

    if Continue.upper() == "N":
        break