def Write(Variable, f):
    """Function to Convert Variables to Strings and Format to write to file with ,"""
    import datetime
    if isinstance(Variable, str) == False:
        if isinstance(Variable, datetime.datetime) == True:
            return f.write(f"{Variable.strftime('%Y-%m-%d')}, ")
        else:
            return f.write(f"{str(Variable)}, ")
    elif isinstance(Variable, str) == True:
        return f.write(f"{(Variable)}, ")


def Write_Space(Variable, f):
    """Function to Convert Variables to Strings and Format to write to file with Space"""
    import datetime
    if isinstance(Variable, str) == False:
        if isinstance(Variable, datetime.datetime) == True:
            return f.write(f"{Variable.strftime('%Y-%m-%d')}\n")
        else:
            return f.write(f"{str(Variable)}\n")
    elif isinstance(Variable, str) == True:
        return f.write(f"{(Variable)}\n")


# asdfasdfasdfasdf
import datetime
CLAIM_NUM = 34
HST_RATE = .15
while True:
    EmpNum = input("Enter the employee number (END to quit): ")
    if EmpNum.upper() == "END":
        break
    EmpName = "John Doe"
    Location = "Stephenville"
    StartDate = "2021-10-27"
    EndDate = "2021-10-30"
    # Calculate the number of days later in the program
    OwnRent = "R"
    if OwnRent == "O":
        KMTravelled = 1400
    StartDate = datetime.datetime.strptime(StartDate, "%Y-%m-%d")
    EndDate = datetime.datetime.strptime(EndDate, "%Y-%m-%d")
    NumDays = (EndDate - StartDate).days
    PerDiem = 300.00
    MilAmt = 168.00
    ClaimAmt = PerDiem + MilAmt
    HST = ClaimAmt * HST_RATE
    ClaimTotal = ClaimAmt + HST
    print(CLAIM_NUM)
    print(EmpName)
    print(Location)
    print(StartDate)
    print(EndDate)
    print(NumDays)
    print(PerDiem)
    print(MilAmt)
    print(ClaimAmt)
    print(HST)
    print(ClaimTotal)
    # Write to a file called Claims.dat.  Need to Open the file, process or write
    # the data to the file, then close the file.
    f = open("Claims.dat", "a")  # "a" adds to the end, "w" overwrites.
    Write(CLAIM_NUM, f)
    Write(EmpNum, f)
    Write(EmpName, f)
    Write(Location, f)
    Write(StartDate, f)
    Write(EndDate, f)
    Write(NumDays, f)
    Write(PerDiem, f)
    Write(MilAmt, f)
    Write(ClaimAmt, f)
    Write(HST, f)
    Write_Space(ClaimTotal, f)
    f.close()
    # All values must be strings.  convert all numbers with str() and all dates with .strftime()
    print()
    print("Claim information has been saved.")
    CLAIM_NUM += 1   # CLAIM_NUM = CLAIM_NUM + 1

    # a test on deleting lines
    #with open("target.txt", "r+") as f:
    #   d = f.readlines()
    #    f.seek(0)
    #    for i in d:
    #        if i != "line you want to remove...":
    #            f.write(i)
    #    f.truncate()