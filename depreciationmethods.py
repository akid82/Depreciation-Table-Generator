# Information on Depreciation Methods Program
"""
    # This application allows user to calculate depreciation for a long-term asset.
    # Depreciation is the process of allocating the appropriate expense related to the cost of a long-term asset over its useful life
    # Depreciation must be calculated in order for businesses to match their expenses with revenues within a single fiscal period
    # This program supports calculation of depreciation with three methods (all GAAP approved)
        1) Straight-Line method
            - Features a constant depreciation expense that is recorded every year throughout the useful life of the asset
            - Depreciation expense per fiscal period is calculated once and recorded each year of the useful life
            
        2) Units of Activity method
            - Based upon the principle that an assets' depreciation is tied to its production of units
            - Features a yearly depreciation expense that is based upon the units the asset produced during that fiscal period
            - Predictions about total and yearly expected output are required

        3) Double Declining method
            - Based upon the principle that an asset will experience a higher amount of wear in the first years of its useful life because newer equipment is generally more efficient
            - Features a yearly depreciation expense that is calculated based on a declining book value of the asset 

    # The date an asset is purchased is important when using the 1) straight-line or 3) double-declining methods
            } When using the Units of Activity method, the purchase date isn't important for calculating the amount of depreciation an asset experiences within a fiscal period 
        - For assets purchased on the first of the fiscal period, a full year of depreciation expense will be recorded every year of the asset's useful life
        - If an asset is purchased any other time throughout the fiscal period, only a portion of the full-year depreciation expense will be recorded in the first and last year of the asset's useful life
            } The depreciation expense for a partial year is calculated based on how many months the asset was held during that fiscal period
                > If an asset is held for 15 or more days in a month, the entire month counts towards the total months of depreciation for that year
                > If an asset is held for less than 15 days in a month, the month is not counted towards the total months of depreciation for that year
            } The ratio of months the asset is held to the total months in the fiscal period is multiplied by the standard depreciation expense calculated for a full year to result in the
            appropriate depreciation expense for the partial year
            
    # With the 2) units of activity and 3) double-declining methods, there is potential for the asset to be completely depreciated to its salvage value before reaching the end of its useful life
        - The straight-line method will result in a depreciaton expense being calculated in every single year of an asset's useful life until reaching its salvage value in the last year
        
"""

# Functions
#------------------------------------------------------------------------

def greeting():
    print('Welcome the the Depreciation Methods Calculation.')

#------------------------------------------------------------------------

def selection():
    print()
    print('Would you like to do: ')
    print('1. Straight-Line Depreciation Method')
    print('2. Units of Activity Depreciation Method')
    print('3. Double Declining Depreciation Method')

    validSelection = False

    while validSelection == False:
        selectedNum = input('Enter the number of the depreciation method you would like to use: ')
        if selectedNum == "1" or selectedNum == "2" or selectedNum == "3":
            validSelection = True
        else:
            print("User must enter 1, 2, or 3\n")
    
    return selectedNum

#------------------------------------------------------------------------

def getInitialCost():

    validInitialCost = False

    while validInitialCost == False:
        try:
            userCost = input('Enter the cost of the asset: ')
            userCost = userCost.strip('$')          # strips any leading $
            if ',' in str(userCost):
                numSplit = str(userCost).split(',')
                userCost = ''.join(numSplit)
            if float(userCost) < 0:      
                print('You must enter a positive amount.')
            elif '.' in str(userCost):     # for user inputs with decimal places
                numSplit = str(userCost).split('.')        # split the number by the decial place
                if len(numSplit[1])>2:                      # if the length of the digits after the decmial point is more than 2, there are too many decimal places
                    print('The principal must be specified in dollars and cents.')
                else:
                    validInitialCost = True
            else:
                validInitialCost = True               # if user input passes all tests, then we can exit while loop and end error checking
        except ValueError:                     # in case we missed anything 
            print('Please enter a number.')
            

    return float(userCost)

#------------------------------------------------------------------------
def getSalvageValue():

    validSalvageValue = False

    while validSalvageValue == False:
        try:
            userSalvageValue = input('Enter the estimated salvage value: ')
            userSalvageValue = userSalvageValue.strip('$')
            if ',' in str(userSalvageValue):
                numSplit = str(userSalvageValue).split(',')
                userSalvageValue = ''.join(numSplit)
            if float(userSalvageValue) < 0:      
                print('You must enter a positive amount.')
            elif '.' in str(userSalvageValue):     # for user inputs with decimal places
                numSplit = str(userSalvageValue).split('.')        # split the number by the decial place
                if len(numSplit[1])>2:                      # if the length of the digits after the decmial point is more than 2, there are too many decimal places
                    print('The principal must be specified in dollars and cents.')
                else:
                    validSalvageValue = True
            else:
                validSalvageValue = True               # if user input passes all tests, then we can exit while loop and end error checkin 
        except ValueError:
            print('Please enter a number.')

    return float(userSalvageValue)
#------------------------------------------------------------------------

def getUsefulLife():

    validUsefulLife = False

    while validUsefulLife == False:
        try:
            userUsefulLife = int(input('Enter the estimated useful life [in years]: '))
            if userUsefulLife < 0:
                print('Please enter a positive number.')
            else:
                validUsefulLife = True
        except ValueError:
            print('Please enter a whole integer number.')

    return userUsefulLife

#------------------------------------------------------------------------

def getPurchaseDate():

    validPurchaseDate = False

    while validPurchaseDate == False:
        try:
            userPurchaseDate = input('Enter the date on which the asset was purchased [mm/dd/yyyy]: ')

            dayMonthYear = userPurchaseDate.split('/')
            year = int(dayMonthYear[2])
            month = int(dayMonthYear[0].lstrip('0'))
            day = int(dayMonthYear[1].lstrip('0'))

            month31days = [1,3,5,7,8,10,12]
            month30days = [4,6,9,11]

            if month > 12 or month < 1:
                print('Please enter a number between 1 and 12 to indicate the month in which the asset was purchased')
            elif month == 2 and day > 28 and year%4 != 0: # February only has 29 days in a leap year (when year is divisible by 4)
                print('February cannot have more than 28 days if not in a leap year')
            elif month == 2 and year%4==0 and day > 29:
                print('February can have up to 29 days in a leap year')
            elif (day == 31) and (month not in month31days):
                print('Month ', month, ' cannot have 31 days')
            elif day > 31:
                print('Months cannot have more than 31 days')
            elif day < 1:
                print('Months cannot have less than 1 day')
            else:
                validPurchaseDate = True
            
        except ValueError:
            print('Please enter a valid date')

    
    return userPurchaseDate

#------------------------------------------------------------------------
def getTotalEstimatedUnits():

    validTotalEstimatedUnits = False

    while validTotalEstimatedUnits == False:
        try:
            userTotalEstimatedUnits = input('Enter the estimated total units to be produced over the life of the asset: ')
            if ',' in str(userTotalEstimatedUnits):
                numSplit = str(userTotalEstimatedUnits).split(',')
                userTotalEstimatedUnits = ''.join(numSplit)
            if int(userTotalEstimatedUnits) < 0:
                print('Please enter a positive number.')
            else:
                validTotalEstimatedUnits = True
        except ValueError:
            print('Please enter a whole number integer value')
    
    return int(userTotalEstimatedUnits)

#------------------------------------------------------------------------

def getUnitsPerYear(totalEstimatedUnits):
    yearUnitList = []
    yearNum = 1
    units = 0
    runningSum = 0

    while runningSum < totalEstimatedUnits:
        validInput = False
        while validInput == False:
            try:
                units = input('How many units are estimated to be produced in Year '+ str(yearNum)+'? ')
                if ',' in str(units):
                    numSplit = str(units).split(',')
                    units = ''.join(numSplit)
                if int(units) < 0:
                    print('Please enter a positive number.')
                else:
                    validInput = True
            except ValueError:
                print('Please enter whole number integer values')

        yearUnitList.append( (yearNum, int(units)) )
        yearNum += 1
        runningSum += int(units)
    
    return yearUnitList

#------------------------------------------------------------------------
def getMonthsOfDepreciation(purchaseDate):
    
    dayMonthYear = purchaseDate.split('/')
    year = int(dayMonthYear[2])
    month = int(dayMonthYear[0].lstrip('0'))
    day = int(dayMonthYear[1].lstrip('0'))

    # Depreciation Duration Determination 
    if '01/01' in purchaseDate:         # if the asset was not purchased on the first day of the year
        monthsOfDepreciation = 12
    else:
        if day <= 15:                   # if asset was purchased on or before the 15th of the month, then an entire month of depreciation is counted
            monthsOfDepreciation = 12 - month + 1           
        else:                           # if asset was purchased after the 15th of the month
            monthsOfDepreciation = 12 - month

    return monthsOfDepreciation

#------------------------------------------------------------------------
def displayHeading():

    column1 = 'Year'
    column2 = 'Net Book Value - Beginning of Year'
    column3 = 'Depreciation Expense Per Year'
    column4 = 'Accumulated Depreciation'
    column5 = 'Net Book Value - End of Year'
    heading = f'{column1:^10}{column2:^40}{column3:^35}{column4:^30}{column5:^30}'
    print(heading)
    print(len(heading)*'=')
    
#------------------------------------------------------------------------
def displayTableStraightLine(cost, usefulLife, salvageValue, depMonths, purchaseDate):
    """ Purchase Date matters in this instance"""

    # Get Year for Table
    dayMonthYear = purchaseDate.split('/')
    year = int(dayMonthYear[2])
    
    # Depreciation Calculation
    firstYearDep = ( (cost - salvageValue)/usefulLife ) * (depMonths/12)     # calculates the depreciation expense for the first year of depreciation 
    depreciationPerYear = (cost - salvageValue)/usefulLife                              # calculates the depreciation expense per year for the straight line method

    # Inital Values
    nbvBOY = cost
    depreciationExpPerYear = firstYearDep
    accumulatedDepreciation = depreciationExpPerYear
    nbvEOY = nbvBOY - depreciationExpPerYear

    # Table Calculations and Printing
    while nbvEOY > salvageValue:
        row = f'{year:^10}{nbvBOY:^40.2f}{depreciationExpPerYear:^35.2f}{accumulatedDepreciation:^30.2f}{nbvEOY:^30.2f}'
        print(row)
        nbvBOY = nbvEOY
        depreciationExpPerYear = depreciationPerYear
        accumulatedDepreciation += depreciationPerYear
        nbvEOY = nbvBOY - depreciationExpPerYear
        year +=1

    # Final Row Calculation         *has to be this way so value of asset doesn't fall below expected salvage value*
    nbvEOY = salvageValue
    depreciationExpPerYear = nbvBOY - nbvEOY
    accumulatedDepreciation = cost - nbvEOY
    row = f'{year:^10}{nbvBOY:^40.2f}{depreciationExpPerYear:^35.2f}{accumulatedDepreciation:^30.2f}{nbvEOY:^30.2f}'
    print(row)
            
#------------------------------------------------------------------------
def displayTableUnitsOfActivity(cost, salvageValue, usefulLife, totalEstimatedUnits, yearUnitList, purchaseDate):
    """ Purchase date does not matter. """

    # Get Year for Table
    dayMonthYear = purchaseDate.split('/')
    year = int(dayMonthYear[2])
    
    # Depreciation Calculation
    depreciationPerUnit = (cost - salvageValue)/totalEstimatedUnits

    # Initialize Values
    nbvBOY = cost
    depreciationExpPerYear = 0
    accumulatedDepreciation = 0
    nbvEOY = 0

    # Table Calculations and Printing
    for tup in yearUnitList:
        depreciationExpPerYear = depreciationPerUnit * tup[1]      # to get the depreciation per year, multiply units (second value in tuple) by the depreciationPerUnit value
        if tup[0] == 1:
            accumulatedDepreciation = depreciationExpPerYear
        else:
            accumulatedDepreciation += depreciationExpPerYear
        nbvEOY = nbvBOY - depreciationExpPerYear
        row = f'{year:^10}{nbvBOY:^40.2f}{depreciationExpPerYear:^35.2f}{accumulatedDepreciation:^30.2f}{nbvEOY:^30.2f}'
        print(row)
        nbvBOY = nbvEOY
        year += 1
    
#------------------------------------------------------------------------
def displayTableDoubleDeclining(cost, usefulLife, salvageValue, depMonths, purchaseDate):
    """ Purchase Date Matters"""

    # Get Year for Table
    dayMonthYear = purchaseDate.split('/')
    year = int(dayMonthYear[2])
    
    # Depreciation Calculation
    straightLinePercentage = (100/usefulLife) / 100      # divide by 100 so percentage is in decimal form
    doubleDepreciationPercentage = straightLinePercentage * 2 

    #Initialize Values
    nbvBOY = cost
    depreciationExpPerYear = doubleDepreciationPercentage * nbvBOY * (depMonths/12)     # calculates the depreciation expense for the first year of depreciation
    accumulatedDepreciation = depreciationExpPerYear
    nbvEOY = nbvBOY - depreciationExpPerYear

    # Table Calculations and Printing
    while nbvEOY > salvageValue:
            row = f'{year:^10}{nbvBOY:^40.2f}{depreciationExpPerYear:^35.2f}{accumulatedDepreciation:^30.2f}{nbvEOY:^30.2f}'
            print(row)
            nbvBOY = nbvEOY
            depreciationExpPerYear = doubleDepreciationPercentage * nbvBOY
            accumulatedDepreciation += depreciationExpPerYear
            nbvEOY = nbvBOY - depreciationExpPerYear
            year += 1

    # Final Row Calculation         *has to be this way so value of asset doesn't fall below expected salvage value*
    nbvEOY = salvageValue
    depreciationExpPerYear = nbvBOY - nbvEOY
    accumulatedDepreciation = cost - nbvEOY
    row = f'{year:^10}{nbvBOY:^40.2f}{depreciationExpPerYear:^35.2f}{accumulatedDepreciation:^30.2f}{nbvEOY:^30.2f}'
    print(row)
    
#------------------------------------------------------------------------
def askYesNo(prompt):
    validAnswer = False
    while validAnswer == False:
        answer = input(prompt)
        if answer[0] == 'y' or answer[0] == 'Y':
            validAnswer = True
            return True
        elif answer[0] == 'n' or answer[0] == 'N':
            validAnswer = True
            return False

#------------------------------------------------------------------------        

# Running
if __name__ == '__main__':
    greeting()
    active = True
    while active:
        choice = selection()
        print()
        cost = getInitialCost()
        salvageValue = getSalvageValue()
        usefulLife = getUsefulLife()
        purchaseDate = getPurchaseDate()
        print()
        if choice == '1':
            depMonths = getMonthsOfDepreciation(purchaseDate)
            displayHeading()
            displayTableStraightLine(cost, usefulLife, salvageValue, depMonths, purchaseDate)
        elif choice == '2':
            totalEstimatedUnits = getTotalEstimatedUnits()
            yearUnitList = getUnitsPerYear(totalEstimatedUnits)
            displayHeading()
            displayTableUnitsOfActivity(cost, salvageValue, usefulLife, totalEstimatedUnits, yearUnitList, purchaseDate)
        elif choice == '3':
            depMonths = getMonthsOfDepreciation(purchaseDate)
            displayHeading()
            displayTableDoubleDeclining(cost, usefulLife, salvageValue, depMonths, purchaseDate)
        print()
        active = askYesNo('Would you like to perform another calculation [y/n]? ')
    print('Quitting Program')        
            


