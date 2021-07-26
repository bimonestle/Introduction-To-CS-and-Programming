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
    # guess = rate / 2
    while guess > 0:
        print('Monthly Salary: %d' % (monthlySalary))
        print('The guess rate: %d' % (guess))
        if guess == rate:
            print('It is not possible to pay the down payment in three years.')
            break

        decimalRate = guess / 10000
        print('decimal rate: %.4f' % (decimalRate))

        monthlySaving = monthlySalary * decimalRate
        print('monthly saving: %d' % (monthlySaving))
        
        currentSavings += monthlySaving + (currentSavings * investmentPerc / 12)
        print(monthlySaving, currentSavings, investmentPerc)
        print('Current savings: %d' % (currentSavings))

        print('High rate: %d' % (guess))
        print('Low rate: %d' % (guess))
        print('Month: %d' % (month))
        print("Bisection steps: %d" % (bisectionSteps))

        if month == (target - 1):
            if currentSavings >= downPayment:
                print('More than downpayment')
                break
        elif month < (target - 1):
            if currentSavings >= downPayment:
                print('Too many months')
                currentSavings = 0
                month = 0
                high = guess
                guess = (high + low) / 2
                bisectionSteps += 1
                monthlySalary = annualSalary / 12


        elif month >= target:
            print('Saving is not sufficient')
            currentSavings = 0
            month = 0
            low = guess
            guess = (high + low) / 2
            bisectionSteps += 1
            monthlySalary = annualSalary / 12

        month += 1
        if month % 6 == 0:
            monthlySalary += (monthlySalary * semiAnnualSalaryRaise)

    print('Number of months to get your dream home: %d months' % (month + 1))
    print('The current savings are %d' % (currentSavings))
    print('The best rate is %.4f' % (guess / 10000))

houseHunting()