# FileName: Lesson 15 Q3
# String methods practice
# Author: Mike Wadden
# Date: October 20, 2021


def Name_Validation(Name):
    """ Function to Validate a Name for Input: Allowing Spaces, - and '"""
    for Char in Name:
        if ("A" <= Char <= "Z" or "a" <= Char <= "z" or Char == " "
                or Char == "-" or Char == "'"):
            continue
        else:
            return False


while True:
    Name = input("Enter Your Name: ")

    if Name == "":
        print("Name cannot be blank: Please Re-Enter")

    elif Name_Validation(Name) == False:
        print("Invalid Name Entered: Please use letters between (a-z), (-) and (') ")
    else:
        break

print(Name)

Validation = True

while True:
    Name = input("Enter Your Name: ")
    for Char in Name:
        if ("A" <= Char <= "Z" or "a" <= Char <= "z" or Char == " "
                or Char == "-" or Char == "'"):
            continue
        else:
            Validation = False

    if Name == "":
        print("Name cannot be blank: Please Re-Enter")

    elif Validation == False:
        print("Invalid Name Entered: Please assured you are useing letter between (a-z), (-) and (') are allowed to be used")
    else:
        break

print(Name)
