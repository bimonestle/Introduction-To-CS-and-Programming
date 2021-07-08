def houseHunting():
    totalCost = int(input('Enter the cost of your dream home: '))
    portionDownPayment = 0.25
    downPayment = portionDownPayment * totalCost
    print("The downpayment of your house is %.2f" % (totalCost * portionDownPayment))

    annualSalary = int(input('Enter your annual salary: '))
    monthlySalary = annualSalary / 12
    print('Your monthly salary is %.2f' % (monthlySalary))

    semiAnnualSalaryRaise = float(input('Enter the semi-annual salary raise, as a decimal: '))

    currentSavings = 0
    investmentPerc = 0.04
    portionSaved = float(input('Enter the percentage of your salary to save, as a decimal: '))
    # monthlySaving = monthlySalary * portionSaved
    # print('Your monthly savings will be %.2f' % (monthlySaving))

    month = 0
    while currentSavings < downPayment:
        monthlySaving = monthlySalary * portionSaved
        currentSavings += monthlySaving + (currentSavings * investmentPerc / 12)
        month += 1
        if month % 6 == 0:
            monthlySalary += (monthlySalary * semiAnnualSalaryRaise)

    print('Number of months to get your dream home: %.2f' % (month))
    print('The current savings are %d' % (currentSavings))

houseHunting()