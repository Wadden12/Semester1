# FileName: QAP1
# Widgets inc requires a program to calculate employee payroll
# Author: Mike Wadden
# Date: September 15,2021

# Program Constants

HOURLY_RATE = 17.50        # Wage Per Hour
COMMISSION_RATE = 0.35          # Commission per Widget
INCOME_TAX_RATE = 0.21          # Income Tax 21%
CPP_RATE = 0.0495          # CPP 4.95%
EI_RATE = 0.016            # EI 1.6%
UNION_DUES = 15            # Union Due per person per pay period

# USER Inputs
Employee_Name = input("Employee Name: ")
Hours_Worked = float(input("Number of Hours Worked: "))
Widgets_Monday = int(input("The Number of Widgets Produced on Monday: "))
Widgets_Tuesday = int(input("The Number of Widgets Produced on Tuesday: "))
Widgets_Wednesday = int(input("The Number of Widgets Produced on Wednesday: "))
Widgets_Thursday = int(input("The Number of Widgets Produced on Thursday: "))
Widgets_Friday = int(input("The Number of Widgets Produced on Friday: "))

# Production Calculations

Total_Widgets = Widgets_Monday + Widgets_Tuesday + Widgets_Wednesday + Widgets_Thursday + Widgets_Friday

# Income Calculations
Regular_Pay = Hours_Worked * HOURLY_RATE
Commission = Total_Widgets * COMMISSION_RATE
Gross_Pay = Commission + Regular_Pay

# Expense Calculations
Income_Tax = Gross_Pay * INCOME_TAX_RATE
CPP = Gross_Pay * CPP_RATE
EI = Gross_Pay * EI_RATE
Total_Deductions = Income_Tax + CPP + EI + UNION_DUES

Net_Pay = Gross_Pay - Total_Deductions

# Display Results

# User Inputed

print()
print("Employee name", Employee_Name)

# Calculated Outputs

print()
print("Total Number of Widgets Produced: ", Total_Widgets,)
print()
print("Regular Pay:      ${:.2f}" .format(Regular_Pay))
print("Commission:       ${:.2f} " .format(Commission))
print("Gross Pay:        ${:.2f}" .format(Gross_Pay))
print()
print("Income Tax:       ${:.2f}" .format(Income_Tax))
print("CPP:              ${:.2f} " .format(CPP))
print("EI:               ${:.2f}" .format(EI))
print("Union Dues:       ${:.2f}" .format(UNION_DUES))
print("Total Deductions: ${:.2f}" .format(Total_Deductions))
print()
print("Net Pay:          ${:.2f}" .format(Net_Pay))
















