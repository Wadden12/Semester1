# FileName: Lesson 21 Q2
# Modern Movie Rentals
# Author: Mike Wadden
# Date: November 3, 2021

#Functions
import datetime
import time

def As_Dollars(Number):
    """Format Dollars amounts to strings"""
    Number_Display = f"${Number:,.2f}"
    return Number_Display


def Write(Variable, f):
    """Function to Convert None Strings to Strings and Format to write to file with ,"""

    if isinstance(Variable, str) == False:
        if isinstance(Variable, datetime.datetime) == True:
            return f.write(f"{Variable.strftime('%Y-%m-%d')}, ")
        else:
            return f.write(f"{str(Variable)}, ")
    elif isinstance(Variable, str) == True:
        return f.write(f"{(Variable)}, ")


def Write_Space(Variable, f):
    """Function to Convert None Strings to Strings and Format to write to file with Space"""

    if isinstance(Variable, str) == False:
        if isinstance(Variable, datetime.datetime) == True:
            return f.write(f"{Variable.strftime('%Y-%m-%d')}\n")
        else:
            return f.write(f"{str(Variable)}\n")
    elif isinstance(Variable, str) == True:
        return f.write(f"{(Variable)}\n")


def Date_Change(Date):
    """Convert Date input (YYYY-MM_DD) into a datetime object"""

    Date = datetime.datetime.strptime(Date, "%Y-%m-%d")
    return Date


#Constants File

# Open Default File and read values into Variables
f = open('Def.txt', 'r')
ACOUNT = int(f.readline())
DCOUNT = int(f.readline())
CCOUNT = int(f.readline())
MCOUNT = int(f.readline())
HCOUNT = int(f.readline())
TAX = float(f.readline())
NEW_RELEASE_WEEKS = int(f.readline())
MOVIE_PULL = int(f.readline())
f.close()

#Input and Validations (END) to close program
while True:
    print("Modern Movie Rentals: Movie Input")
    print()
    print("Enter (END) into Movie Name to Close the Program")
    print()
    Movie_Name = input("Enter the Name of the Movie: ").title().lstrip().rstrip()
    if Movie_Name.upper() == "END":
        print("Good Day")
        break

    while True:
        try:
            Release_Date = input("Enter The Movie Release Date: (YYYY-MM-DD) ")
            Release_Date = Date_Change(Release_Date)
        except:
            print("Invalid Entry: Please Enter Release Dating using YYYY-MM-DD Format")
        else:
            New_Release_End = Release_Date + datetime.timedelta(days=NEW_RELEASE_WEEKS)
            Delete_Date = Release_Date + datetime.timedelta(weeks=MOVIE_PULL)
            break

    while True:
        Movie_Code = input("Enter Movie Type: (A)-Action, (D)-Drama, (C)-Comedy, (M)-Musical, (H)-Horror: ").upper()
        if Movie_Code != "A" and Movie_Code != "D" and Movie_Code != "C" and Movie_Code != "M" and Movie_Code != "H":
            print("Invalid Entry: Please Enter (A)-Action, (D)-Drama, (C)-Comedy, (M)-Musical, (H)-Horror ")
        elif Movie_Code == "":
            print("Movie Type Entry Cannot Be Blank")
        elif Movie_Code == "A":
            Movie_Type = "Action"
            MovieID = f"{Movie_Code}-{ACOUNT}"
            ACOUNT += 1
            break
        elif Movie_Code == "D":
            Movie_Type = "Drama"
            MovieID = f"{Movie_Code}-{DCOUNT}"
            DCOUNT += 1
            break
        elif Movie_Code == "C":
            Movie_Type = "Comedy"
            MovieID = f"{Movie_Code}-{CCOUNT}"
            CCOUNT += 1
            break
        elif Movie_Code == "M":
            Movie_Type = "Musical"
            MovieID = f"{Movie_Code}-{CCOUNT}"
            MCOUNT += 1
            break
        elif Movie_Code == "H":
            Movie_Type = "Horror"
            MovieID = f"{Movie_Code}-{HCOUNT}"
            HCOUNT += 1
            break

    while True:
        Movie_Rating = input("Enter Movie Rating: (G)-General, (P)-Parental Guidance or (R)-Restricted: ").upper().strip()
        if Movie_Rating != "G" and Movie_Rating != "P" and Movie_Rating != "R":
            print("Invalid Entry: Enter (G)-General, (P)-Parental Guidance or (R)-Restricted ")
        else:
            break

    while True:
        try:
            Rental_Price = float(input("Enter Rental Price: $"))
        except:
            print("Invalid Entry: Please Enter the Rental Price Number")
        else:
            if Rental_Price < 1.99 or Rental_Price > 8.99:
                print("Invalid Entry for Rental Price: The price must be between $1.99-$8.99")
            else:
                break

    #Processing

    Hst = Rental_Price * TAX
    Rental_Total = Rental_Price + Hst

    print()
    print("Movie Details")
    print()
    print("Code:", MovieID)
    print("Name: ", Movie_Name)
    print("Release Date:", Release_Date.date())
    print("Type: ", Movie_Type)
    print("Rating: ", Movie_Rating)
    print("Rental Price: ", As_Dollars(Rental_Total))
    print("New Release Status End Date: ", New_Release_End.date())
    print("Date for the Movie to be Pulled off the Shelf ", Delete_Date.date())
    print()

    #Writing Files
    f = open('Movie.txt', 'a')
    Write(MovieID, f)
    Write(Movie_Name, f)
    Write(Movie_Type, f)
    Write(Movie_Rating, f)
    Write(Rental_Total, f)
    Write(New_Release_End, f)
    Write_Space(Delete_Date, f)
    f.close()

    # Transition between entries
    Wait_Message = f"{Movie_Name} Successfully Saved!"
    Time = 2 / len(Wait_Message)

    print()
    for i in Wait_Message:
        print(i, end='')
        time.sleep(Time)
    print()
    print()
    print("*********************************************")
    AnyKey = input("Press any key to Continue....")
    print()

# Updating the Counter
f = open('Def.txt', 'w')
Write_Space(ACOUNT, f)
Write_Space(DCOUNT, f)
Write_Space(CCOUNT, f)
Write_Space(MCOUNT, f)
Write_Space(HCOUNT, f)
Write_Space(TAX, f)
Write_Space(NEW_RELEASE_WEEKS, f)
Write_Space(MOVIE_PULL, f)
f.close()