import sys

sys.path.append("./Functions")

from Functions import formatters

Title = "Mr."
First_Name = "J%o$$h!n!! Wa!d#den!"
Last_Name = "John Smith"

import re


def Name_Validation_Two(Name):
    return re.match("(?m)^[A-Za-z -']+$", Name) is not None


def New_Name_Validation(First_Name):
    """Function Validates a name and removes unwanted entries"""
    First_Name = formatters.split(First_Name)
    New_First_Name = []
    for char in First_Name:
        if formatters.Name_Validation(char) == True:
            New_First_Name.append(char)
    First_Name = ''.join(New_First_Name)
    return First_Name


print(New_Name_Validation(First_Name))
print(New_Name_Validation(Last_Name))

print(Name_Validation_Two(First_Name))
print(Name_Validation_Two(Last_Name))
