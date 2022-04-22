def As_Dollars(Number):
    """Format Dollars amounts to strings"""
    Number_Display = f"${Number:,.2f}"
    return Number_Display

#  For Loop For Monthly Payment Display
Total_Price = 15000
print()
AnyKey = input("Press any key to Display Financing Options....")
print()
print("# Years   # Payments   Financing Fee   Total Price  Monthly Payment")

for Years in range(1, 5):  # Loop to show  different monthly payments for the customer to choose

    New_Price = Total_Price
    Payment = 12 * Years
    Financing_Fee = 39.99 * Years  # Financing Fee $39.99
    New_Price += Financing_Fee
    Monthly_Payment = New_Price / Payment

    print(
        F"    {Years:1}          {Payment:2}       {As_Dollars(Financing_Fee):>10}      {As_Dollars(New_Price):10}      {As_Dollars(Monthly_Payment):>10}")

print()

while True:
    try:
        Pay_Plan = int(input("Enter the payment schedule you want to follow (1-4): #"))
    except:
        print("Invlaid Entry: Please Enter a number Between 1-4 ")
    else:
        if Pay_Plan < 1 or Pay_Plan > 4:
            print("Invalid Entry Select a payment schedule between (1-4 ")
        else:
            break



