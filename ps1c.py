def houseHunting():
    totalCost = int(input('Enter the cost of your dream home: '))
    dpRate = 0.25
    downPayment = dpRate * totalCost
    print("The downpayment of your house is %.2f" % (downPayment))

    annualSalary = int(input('Enter your annual salary: '))
    monthlySalary = annualSalary / 12
    print('Your monthly salary is %.2f' % (monthlySalary))


    currentSavings = 0
    investmentPerc = 0.04
    semiAnnualSalaryRaise = 0.07
    month = 0
    target = 36
    bisectionSteps = 0
    rate = 10000
    low = 0
    high = rate
    guess = (high + low) / 2
    while currentSavings < downPayment:
        decimalRate = guess / 10000
        monthlySaving = monthlySalary * decimalRate
        currentSavings += monthlySaving + (currentSavings * investmentPerc / 12)

        print('Current savings: %d' % (currentSavings))
        print('High rate: %d' % (guess))
        print('Low rate: %d' % (guess))

        if month < target and currentSavings > downPayment:
            currentSavings = 0
            high = guess
            guess = (high + low) / 2
            bisectionSteps += 1
            # month = 0
        elif month > target and currentSavings < downPayment:
            currentSavings = 0
            low = guess
            guess = (high + low) / 2
            bisectionSteps += 1
            # month = 0

        month += 1
        if month % 6 == 0:
            monthlySalary += (monthlySalary * semiAnnualSalaryRaise)

    print('Number of months to get your dream home: %.2f' % (month))
    print("Bisection steps: %d" % (bisectionSteps))
    print('The current savings are %d' % (currentSavings))

houseHunting()