import math
def As_Dollars(Number):
    """Format Dollars amounts to strings"""
    Number_Display = f"${Number:,.2f}"
    return Number_Display


Q1 = 9 +(12/6) **2 + (2 * -9) - 5
print("Q1: ", Q1)

Q2= (28+7)/-7*(5-6)**2 - 1
print("Q2:", Q2)

Q3= ((4+3)*4) - 5 + ((7-4)**2/3) +1
print("Q3:", Q3)

Q4a = 38.63 + 14.2
print("Q4a:", Q4a)

Q4b = 230 * 2.465
print("Q4b:", Q4b)

Q4c = 13.2 / 4.8
print("Q4c:", Q4c)

Q5 = 38.63 + 14.2
print("Q5:", Q5)

Q9 = (3.5 + 5 + 6.5) * 12.50
print("Student Earned ", As_Dollars(Q9))

Q10 = (5.5 + 7.75) - 3.25
print(f"George has {Q10} yards left")

#Q11
Food = 475
Per = .12
Budget = 475/.12
print(f"The total Miler Family Budget is {As_Dollars(Budget)}")

#Q12

Budget = 18000
Spend_Per = .09
Spend = Budget * Spend_Per
print(f"{As_Dollars(Spend)} of the budget was used")

#Q13

Retail_Price = 219.95
Hst = .15
Total = Retail_Price * (1 + Hst)
print(f"The Total Price of the Skies is {As_Dollars(Total)}")

#Q14

Sample1 = 2.6
Sample2 = 2.9

Percent = (Sample2 - Sample1) / Sample1
Percent *= 100
print(f"The Percentage increase is {Percent:.3f}%")

#Q15

Used = 320
Tank = 1600

Fuel = (Tank - Used) / Tank
Fuel *= 100
print(f"The Percentage of remaining fuel is {Fuel:.0f}%")

#16

Total = 345
Hst = .15
Sell_Price = 345 / (1.15)
Tax = Sell_Price * Hst
print(f"The Sell Price of the Harnes is {As_Dollars(Sell_Price)} and Tax is {As_Dollars(Tax)}")

#17

Price1 = 60
Price2 = 36

Percent = (Price1 - Price2) / Price1
Percent *= 100
print(f"The percent decrease of cost is {Percent:.0f}%")

#18a
print()
print("18b")
for x in range(-3,4):
    y = 3*x - 9
    print("X =", x)
    print("Y =", y)


#18b
print()
print("18b")
for x in range(-3,4):
    y = (12 - 5*x) /2
    print("X =", x)
    print("Y =", y)

#18c
print()
print("18c")
for x in range(-3,4):
    y = -.5 * x**2 -3*x + 5
    print("X =", x)
    print("Y =", y)

#18d
print()
print("18d")
for x in range(5,13):
    y = math.sqrt(3*x-4) -2
    print("X =", x)
    print(f"Y = {y:.3f}")

#19a

# Triangle1
base = 3
height = 9
side = base**2 + height**2
T1 = math.sqrt(side)
print(f"Tri A side = {T1}")

# Triangle2
base = 4.5
height = 5
side = base**2 + height**2
T2 = math.sqrt(side)
print(f"Tri B side = {T2}")


P = T2 + T2 + 12 + T1 + 15
print(f"Perimter is {P:.3f}")

Base = 9
Height = 5
AreaT1 = (Base/2) * Height
print("Area T1 = ", AreaT1)

Base = 3
Height = 9
AreaT2 = (Base/2) * Height
print("Area T2 = ", AreaT2)

Length = 12
Width = 9
Area_Rec =  Length * Width
print("Area of Rec = ", Area_Rec)

Total_Area = AreaT1 + AreaT2 + Area_Rec

print("Total Area: ", Total_Area)


# Triangle
base = 10
height = 9
side = base**2 + height**2
T2 = math.sqrt(side)
print(f"Tri side = {T2}")

P = 15 + 15 + 13.45 + 6 + 6.5 + 30.85 + 6.5
print(f"The Total Perimter is {P:.2f}")

Area_Sqare = 15**2
print(f"Area of the Sqaure: {Area_Sqare:.2f}")
Area_Circle = (math.pi * 6**2)/2
print(f"Area of the Circle: {Area_Circle:.2f}")
Area_Rec = 10 * 6
print(f"Area of Rectangle: {Area_Rec:.2f}")
Area_Triangle = (10/2) * 9
print(f"Area of Triangle: {Area_Triangle:.2f}")
Total_Area = Area_Sqare + Area_Circle + Area_Rec + Area_Triangle
print(f"Total Area: {Total_Area:.2f}")

# math.sqrt() is used to calculate the square root of a number
Sqaure_Root = math.sqrt(10) #Gets the Square Root of 10

# math.pi Represents pi which is used in geogmetry forumulas(Is more accurate than useing 3.142.
AreaCircle = (math.pi * 6**2)/2 #used in the forumat for calculating a semi circle

# math.trunc() is used to change a float into a intergar(ie Remove decimals places)

x = 153.91095641
Truncate = math.trunc(x)  #removes decimal places
print("Truncate: ", Truncate)

print(math.floor(x)) # Rounds down for example x would be 153
print(math.ceil(x))  #Round up for example x would be 154

x = math.ceil(x) - 0.05 # Ceil and Floor can be used in Retail to set price at .99 or .95
print(x)