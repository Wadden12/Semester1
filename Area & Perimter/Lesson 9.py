#Practice Area & Prem

PI = 3.14
Base = 22.2
Height = 11.5
Radius = 12.1

# Q1 Perimeter are done wrong lol
print()
Perm_Rect = (2 * Base) + (2 * Height)
Perm_Circle = (2 * PI * Radius) / 4
print("Perimeter of the Rectangle:", Perm_Rect)
print("Perimeter of the 1/4 Circle:", Perm_Circle)
Perm_Total = Perm_Circle + Perm_Rect
print("*" * 40)
print("A1. Total Perimeter", Perm_Total)
print("*" * 40)
#Q1 Area

Area_Rec = Base * Height
Area_Circle = (PI * Radius ** 2) / 4             #Divide by 4 because of 1/4 Circle
print("Area of Th Rectangle: ",Area_Rec)
print("Area of the 1/4 Circle: ", Area_Circle)
Total_Area = Area_Rec + Area_Circle
print("*" * 40)
print("A1. Total Area: ", Total_Area)
print("*" * 40)

#Q2 Perimeter

Base = 20.2
Height = 3.1
Radius = 10.1

Perm_Rect = (2 * Base) + (2 * Height)
Perm_Circle = (2 * PI * Radius) / 2             #Divide by 2 because half Circle
print("Perimeter of the Rectangle:", Perm_Rect)
print("Perimeter of the 1/2 Circle:", Perm_Circle)
Perm_Total = Perm_Circle + Perm_Rect
print("*" * 40)
print("A2. Total Perimeter", Perm_Total)
print("*" * 40)

#Q2 Area

Area_Rec = Base * Height
Area_Circle = (PI * Radius ** 2) / 2            #Divide by 4 because of 1/2 Circle
print("Area of Th Rectangle: ",Area_Rec)
print("Area of the 1/4 Circle: ", Area_Circle)
Total_Area = Area_Rec + Area_Circle
print("*" * 40)
print("A2. Total Area: ", Total_Area)
print("*" * 40)

#Q3 Perimeter

A_Sq = 11.1
A_Tri = 12.1
B_Tri = 11.1
Base = 11.1
Height = 11.4

Perm_Sqaure = 4 * A_Sq
Perm_Tri = 2 * A_Tri + B_Tri
print("Perimeter of Sqaure: ",Perm_Sqaure)
print("Perimeter of Triangle ", Perm_Tri)
Total_Perm = Perm_Sqaure + Perm_Tri
print("*" * 40)
print("A3. Total Perimeter: ", Total_Perm)
print("*" * 40)

#Q3 Area

Area_Sqaure = A_Sq ** 2
Area_Tri = (.5 * Base) * Height
print("*" * 40)
print("Area of the Square:", Area_Sqaure)
print("Area of the Triangle:", Area_Tri)
Total_Area = Area_Sqaure + Area_Tri
print("*" * 40)
print("3. Total Area:", Total_Area)


#Q4

Base = 20.1
Height = 6.1

Perm_Rect = (2 * Base) + (2 * Height)
print("Perimeter Rectangle:", Perm_Rect)
Area_Rec = Base * Height
print("Area Rectangle: ", Area_Rec)
print("*" * 40)

A = 1.1   #Base
B = 4.1
C = 3.0   #Height

Perm_Tri = ( A + B + C) * 2
print("Perimeter Triangle: ", Perm_Tri)
Area_Tri = ((0.5 * A) * C) * 2
print("Area of Triangle: ", Area_Tri)
print("*" * 40)

Total_Perm = Perm_Rect + Perm_Tri
Total_Area = Area_Rec + Area_Tri
print("4. Total Perimeter: ", Total_Perm)
print("4. Total Area: ", Total_Area)
print("*" * 40)
#Q5

Base = 18.1
Height = 9.3

Perm_Rect = (2 * Base) + (2 * Height)
print("Perimeter Rectangle:", Perm_Rect)
Area_Rec = Base * Height
print("Area Rectangle: ", Area_Rec)
print("*" * 40)

A = 4.3   #Base
B = 11.1
C = 9.3   #Height

Perm_Tri = ( A + B + C) * 2
print("Perimeter Triangle: ", Perm_Tri)
Area_Tri = ((0.5 * A) * C) * 2
print("Area of Triangle: ", Area_Tri)
print("*" * 40)

A = 18.1  #Base
B = 12.1
Height = 9.0

Perm_Tri2 = ( 2 *A + B)
print("Perimeter Triangle2: ", Perm_Tri2)
Area_Tri2 = ((0.5 * A) * Height)
print("Area of Triangle2: ", Area_Tri2)
print("*" * 40)

Total_Perm = Perm_Rect + Perm_Tri + Perm_Tri2
Total_Area = Area_Rec + Area_Tri + Area_Tri2
print("5.Total Perimeter: ", Total_Perm)
print("5.Total Area: ", Total_Area)
print("*" * 40)

#Q6

Base = 21.2
Height = 9.8

Perm_Rect = (2 * Base) + (2 * Height)
print("Perimeter Rectangle:", Perm_Rect)
Area_Rec = Base * Height
print("Area Rectangle: ", Area_Rec)
print("*" * 40)

A = 10  #Base
B = 11
C = 11.1   #Height

Perm_Tri = ( A + B + C)
print("Perimeter Triangle: ", Perm_Tri)
Area_Tri = ((0.5 * A) * C)
print("Area of Triangle: ", Area_Tri)
print("*" * 40)

Radius = 10.1

Perm_Circle = (2 * PI * Radius) / 4
print("Perimeter of the 1/4 Circle:", Perm_Circle)
Area_Circle = (PI * Radius ** 2) / 4             #Divide by 4 because of 1/4 Circle
print("Area of the 1/4 Circle: ", Area_Circle)
print("*" * 40)

Total_Perm = Perm_Rect + Perm_Tri + Perm_Circle
Total_Area = Area_Rec + Area_Tri + Area_Circle
print("6. Total Perimeter:", Total_Perm)
print("6.Total Area: ", Total_Area)




