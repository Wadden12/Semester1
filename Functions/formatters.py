# filename: formatters.py
# Author: Mike Wadden
# Practice Functions
# Date October 14, 2021


def As_Dollars(Number):
    """Format Dollars amounts to strings"""
    Number_Display = f"${Number:,.2f}"
    return Number_Display


def Weight_In_Pounds(Weight):
    """Format Weight into Pounds String"""
    if Weight < 0 :
        raise ValueError("Number Cannot Be Negative")
    Weight_Display = f"{Weight} lbs"
    return Weight_Display


def Name_Validation(Name):
    """ Function to Validate a Name for Input: Allowing Spaces, - and '"""
    for Char in Name:
        if ("A" <= Char <= "Z" or "a" <= Char <= "z" or Char == " "
                or Char == "-" or Char == "'"):
            continue
        else:
            return False
    return True


def split(Text):
    """Function to Spilt individual words"""
    return list(Text)



def Date_Change(Date):
    """Convert Date input (YYYY-MM_DD) into a datetime object"""
    import datetime
    Date = datetime.datetime.strptime(Date, "%Y-%m-%d")
    return Date


def Write(Variable, f):
    """Function to Convert None Strings to Strings and Format to write to file with ,"""
    import datetime
    if isinstance(Variable, str) == False:
        if isinstance(Variable, datetime.datetime) == True:
            return f.write(f"{Variable.strftime('%Y-%m-%d')},")
        else:
            Variable = round(Variable, 2)
            return f.write(f"{str(Variable)},")
    elif isinstance(Variable, str) == True:
        return f.write(f"{(Variable)},")


def Write_Space(Variable, f):
    """Function to Convert None Strings to Strings and Format to write to file with Space"""
    import datetime
    if isinstance(Variable, str) == False:
        if isinstance(Variable, datetime.datetime) == True:
            return f.write(f"{Variable.strftime('%Y-%m-%d')}\n")
        else:
            Variable = round(Variable, 2)
            return f.write(f"{str(Variable)}\n")
    elif isinstance(Variable, str) == True:
        return f.write(f"{(Variable)}\n")

def Format_Phone(Phone):
    """Function to Format a Phone Number into (999)-999 9999)"""
    Phone = str(Phone)
    return f"({Phone[0:3]}) {Phone[3:6]}-{Phone[6:10]}"

def Business_Day(Date):
    """Function to Work Within Business Days Only Mon-Fri"""
    import datetime
    Weekday = Date.weekday()
    if Weekday == 5:
        Date += datetime.timedelta(days=2)
    elif Weekday == 6:
        Date += datetime.timedelta(days=1)
    return Date

def Clear():
    """Function to Clear Terminal Output"""
    import os
    from sys import platform

    if platform == "linux" or platform == "linux2":  #Linux2
        return os.system('clear')
    elif platform == "darwin":  #OS X
        return os.system('clear')
    elif platform == "win32":     #Windows
        return os.system('cls')

def Check_Email(Email):
    """Validates a Email Input"""
    import re

    Check = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    if re.fullmatch(Check, Email):
        return True
    else:
        return False

def No_Space_Int(Digit):
    """Removes any spaces when a user inputs Int digit"""
    Digit = str(Digit).strip()
    Digit = int(Digit)
    return Digit

def As_Dollars_Pad(Number):
    """Format Dollars amounts to strings & Pad Right 10 Spaces"""
    Number_Display = f"${Number:,.2f}"
    Number_Display = f"{Number_Display:>10}"
    return Number_Display

def Number_Pad(Number):
    """Format Dollars amounts to strings & Pad Right 10 Spaces"""
    Number_Display = f"{Number:,}"
    Number_Display = f"{Number_Display:>10}"
    return Number_Display

def Feet_To_Meters(Feet):
    """Converts Feet into Meters"""
    Meter = Feet * 3.28084
    return Meter
