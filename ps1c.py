def houseHunting():
    totalCost = int(input('Enter the cost of your dream home: '))
    portionDownPayment = 0.25
    downPayment = portionDownPayment * totalCost
    print("The downpayment of your house is %.2f" % (totalCost * portionDownPayment))

    annualSalary = int(input('Enter your annual salary: '))
    monthlySalary = annualSalary / 12
    print('Your monthly salary is %.2f' % (monthlySalary))


    currentSavings = 0
    investmentPerc = 0.04
    semiAnnualSalaryRaise = 0.07
    month = 0
    target = 36
    bisectionSteps = 0
    portionSaved = 10000
    while month < target:
        decimalPortion = portionSaved / 10000
        monthlySaving = monthlySalary * decimalPortion
        currentSavings += monthlySaving + (currentSavings * investmentPerc / 12)
        
        if month < target and monthlySaving > downPayment:
            bisectionSteps += 1

        month += 1
        if month % 6 == 0:
            monthlySalary += (monthlySalary * semiAnnualSalaryRaise)


    print('Number of months to get your dream home: %.2f' % (month))
    print('The current savings are %d' % (currentSavings))

houseHunting()