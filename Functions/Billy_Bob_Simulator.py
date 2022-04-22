# filename: Billy_Bob_Simulator
# Author: Mike Wadden
# Practice Billy Bob Evil Master Plan Scrambler
# Date October 14, 2021


#Input

while True:
    Sentence = input("Type anything to Test Billy Bob's System: ").lower()
    if Sentence == "":
        print("Input Cannot be Blank!")
    else:
        break

# Function to spilt the text of individual words
Word_List = []
Final_List = []

def split(Text):
    """Function to Spilt individual words"""
    return list(Text)


def Word_Scrambler(String):
    """A Evil Scrambler created to lower case words and convert each word indivudlar letters into alphabetical order"""

    Words = String.split(" ")

    for word in Words:
        Split = split(word)
        Split.sort(reverse=True)
        Word_List.append(Split)

    for Combine in Word_List:
        Combine.sort()
        Join = ''.join(Combine)
        Final_List.append(Join)

    return Final_List

print()
print("Original Text: ", Sentence)
print()
print(f"Scrambled Text:{Word_Scrambler(Sentence)}")





