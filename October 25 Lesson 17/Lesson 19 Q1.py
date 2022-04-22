# FileName: Lesson 19
# Function To Calculate Gross Pay
# Author: Mike Wadden
# Date: October 26, 2021

def As_Dollars(Number):
    """Format Dollars amounts to strings"""
    Number_Display = f"${Number:,.2f}"
    return Number_Display


def Gross_Pay(Hours_Work, Hour_Pay, OT = 1.5):
    """Function to Calculate Gross Pay of a Employee w/ Overtime"""

    if Hours_Work <= 40:
        Pay = Hours_Work * Hour_Pay
    if Hours_Work > 40:
        Pay = (40 * Hour_Pay) + ((Hours_Work - 40) * (Hour_Pay * OT))
    print(As_Dollars(Pay))

Gross_Pay(46, 10.00)


def Sale_Bonus(TSales, BONUS_Rate = 0.01, BONUS_Extra = 500):    #Constants In CAPS     0):    #Constants In CAPS
    """ Function to Calculate a Bonus for a Sales Rep"""                                
    if TSales < 5000:                                                                   
        Bonus = 0                                                                       
    elif TSales > 5000:                                                                 
        Bonus = TSales * BONUS_Rate                                                     
    if TSales > 10000:                                                                  
        Bonus += BONUS_Extra                                                            
                                                                                        
    print(f" The Sales Rep Bonus is {As_Dollars(Bonus)}")                               

Sale_Bonus(15000)


def The_Sum(*input):
    """ Sums all numbers up to and including Values passed"""
    Total = 0
    for sum in input:
        Total += sum
    return Total

print(The_Sum(1,2,3,4,5,6,7,8,9,10))


def As_Dollars_Pad(Number):
    """Format Dollars Amounts to strings & Pad Right"""
    Number_Display = f"${Number:,.2f}"
    Number_Display = f"{Number_Display:>15}"
    return Number_Display

Sales = 15000

print(As_Dollars_Pad(Sales))
print(As_Dollars(Sales))


def Employe_Discount(Item_Cost):
    """ Function to calculate the Employee Discount on a Item"""
    #Constants
    EMP_DIS = 0.30       #30% Discount on items less than $1,000
    EMP_DIS2 = 0.40      #40% Discount on items more than $1,000
    TAX_RATE = 0.15
    ENV_RATE = 0.02

    if Item_Cost < 1000:
        Discount_Cost = Item_Cost * (1 - EMP_DIS)
    else:
        Discount_Cost = Item_Cost * (1 - EMP_DIS2)

    Hst = Item_Cost * TAX_RATE
    Env_Tax = Discount_Cost * ENV_RATE
    Total_Cost = Discount_Cost + Hst + Env_Tax

    return Total_Cost

print(As_Dollars(Employe_Discount(1500)))


# The function can be used if the user enters a employee code then the program applies the function to lower the cost.

    
