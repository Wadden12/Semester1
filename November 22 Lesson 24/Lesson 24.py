# FileName: Lesson 24
# Report Creating
# Author: Mike Wadden
# Date: November 22, 2021



# Print Main Headings and Column headings

print("The Company Name")
print("Description of this report")
print()
print(" Emp  Emp Name            Item      HST      Total")
print(" No                       Cost               Cost")
print("=" * 51)

# Set totals for counters and accumulators to 0
EmployeeCtr = 0
ItemCostAcc = 0
HSTAcc = 0
TotalCostAcc = 0

# Process the file - Open / Process the lines in a loop / Close
f = open("Sales.dat", "r")
for SalesDataLine in f:
    SalesLine = SalesDataLine.split(",")
    EmpNum = SalesLine[0]
    EmpName = SalesLine[1].strip()
    ItemCost = float(SalesLine[2].strip())
    HST = float(SalesLine[3].strip())
    TotalCost = float(SalesLine[4].strip())
    print(" {} {:<20} ${:,.2f}   ${:,.2f}   ${:,.2f}".format(EmpNum, EmpName, ItemCost, HST, TotalCost))

    # Update the counters and accumulators
    EmployeeCtr += 1
    ItemCostAcc += ItemCost
    HSTAcc += HST
    TotalCostAcc += TotalCost
f.close()
# Print the totals based on the counters and accumulators.
print("=" * 51)
print("Employees listed: {}    ${:,.2f}  ${:,.2f} ${:,.2f}".format(EmployeeCtr, ItemCostAcc, HSTAcc, TotalCostAcc))
print()
print("                 End of Listing")