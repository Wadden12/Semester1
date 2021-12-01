# FileName: Lesson 28
# Quiz Grade
# Author: Mike Wadden
# Date: November 30, 2021

# Functions

def Name_Validation(Name):
    """ Function to Validate a Name for Input: Allowing Spaces, - and '"""
    for Char in Name:
        if ("A" <= Char <= "Z" or "a" <= Char <= "z" or Char == " "
                or Char == "-" or Char == "'"):
            continue
        else:
            return False
    return True


def Quiz_Answer_Check(Question, Key, Answers):
    """ Function to check the Quiz Answers"""
    Index = 0
    Q = 0
    Correct = 0
    while Q != Question:

        if Key[Index] == Answers[Index]:
            Correct += 1
        Q += 1
        Index += 1
    Grade = int((Correct / Question) * 100)
    return Correct, Grade


def Student_Answer(Question):
    """ Function to input the Student Answers"""
    while True:
        print()
        print("Enter Student Answers for the Quiz")
        print()
        Question_Count = Question
        Answer = []
        i = 0
        while Question_Count != 0:
            # set up a loop to enter questions

            Student_Answer = input(f"Question: {i + 1} ").upper().strip()
            Answer.append(Student_Answer)
            i += 1
            Question_Count -= 1

            if Student_Answer != "A" and Student_Answer != "B" and Student_Answer != "C" and Student_Answer != "D":
                print("invalid Entry: Please Enter A,B,C,D")
                print()
                Question_Count += 1
                i -= 1
                Answer.pop()

        # Display Key Answers
        i = 0
        print()
        for a in Answer:
            i += 1
            print(f"{i}.{a}")

        while True:
            print()
            Confirmation = input("Is the Student Answers Correct?  (Y) or (N) ").upper()
            if Confirmation.upper() == "Y":
                break
            elif Confirmation.upper() == "N":
                print()
                break
            else:
                print("Incorrect Value entered, Please Enter Y or N")

        if Confirmation == "Y":
            break

    return Answer

def Student_Name():
    """Function to enter and Validate a Student Name"""
    while True:
        print()
        Student_First = input("Enter Student First Name: ").title().lstrip().rstrip()
        if Student_First == "":
            print("First Name cannot be blank: Please Re-Enter")
        elif len(Student_First) >15:
            print("Invalid Name Length: Cannot be longer than 15 letters ")
        elif Name_Validation(Student_First) == False:                              #Function to Validate Name Input
            print("Invalid Name Entered: Please use letters between (a-z), (-) and (') ")
        else:
            break
    return Student_First


# inputs
print()
print("Quizz Information & Key Answer Key")
print()

Quiz_Name = input("Enter The Quiz Name: ").title()

while True:
    #Confirm Key Answers
    while True:
        try:
            Question = int(input("Enter the number of questions on the Quiz: "))
        except:
            print("Invalid Entry: Please Enter the Number of Questions on the Quiz: ")
        else:
            if Question < 5:
                print("Invalid Entry: There must be 5 questions on the Quiz")
            else:
                break

    # Input Key_Answer Key
    print()
    print("Enter Answer Key for the Student Quiz")
    print()
    Key = []
    i = 0
    Question_Count = Question
    while Question_Count != 0:
        # set up a loop to enter questions
        Key_Answer = input(f"Question: {i + 1} ").upper().strip()
        Key.append(Key_Answer)
        i += 1
        Question_Count -= 1

        if Key_Answer != "A" and Key_Answer != "B" and Key_Answer != "C" and Key_Answer != "D":
            print("invalid Entry: Please Enter A,B,C,D")
            print()
            Question_Count += 1
            i -= 1
            Key.pop()

    # Display Key Answers
    i = 0
    print()
    for k in Key:
        i += 1
        print(f"{i}.{k}")

    while True:
        print()
        Confirmation = input("Is the Key Answer Key Correct?  (Y) or (N) ").upper()
        if Confirmation.upper() == "Y":
            break
        elif Confirmation.upper() == "N":
            print()
            break
        else:
            print("Incorrect Value entered, Please Enter Y or N")

    if Confirmation == "Y":
        break
print()
print("Grading Inputs:")
print()

while True:
    # Quizz Number Validation Loop
    try:
        Quizz_Number = int(input("Enter the Number of Quizzes to be graded: "))
    except:
        print("Invalid Entry: Please enter the number of Quizzes to be graded: ")
    else:
        if Quizz_Number < 1:
            print(" The Number of Quizzes cannot be less than 1 ")
        else:
            break

# Output Headings
print("-" * 35)

# Loop Length
Quizz_Count = Quizz_Number
Student_List = []
Correct_List = []
Grade_List = []

while Quizz_Count != 0:

    Name = Student_Name()
    Answer = Student_Answer(Question)
    Temp = Quiz_Answer_Check(Question,Key,Answer)
    Correct = Temp[0]
    Grade = Temp[1]
    Student_List.append(Name)
    Correct_List.append(Correct)
    Grade_List.append(Grade)
    Quizz_Count -= 1

Student_Count = Quizz_Number


index = 0
# Output
print()
print(f"Quiz: {Quiz_Name}")
print()
print("Student       #Correct     %Grade")
print("-" * 35)
while Student_Count != 0:
    print(f"{Student_List[index]:15} {Correct_List[index]:<2}           {Grade_List[index]:<3}")
    Student_Count -= 1
    index += 1

Average = int(sum(Grade_List)/Quizz_Number)
print("-" * 35)
print(f"Class Average is {Average}%")






