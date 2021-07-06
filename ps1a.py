# Write a program to calculate how many months it will take you to save up enough money for a down
# payment. You will want your main variables to be floats, so you should cast user inputs to floats.

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
    portionSaved = float(input('Enter the percentage of your salary to save, as a decimal: '))
    monthlySaving = monthlySalary * portionSaved
    print('Your monthly savings will be %.2f' % (monthlySaving))

    month = 0
    while currentSavings < downPayment:
        currentSavings += monthlySaving + (currentSavings * investmentPerc / 12)
        month += 1

    print('Number of months to get your dream home: %.2f' % (month))
    print('The current savings are %d' % (currentSavings))

houseHunting()