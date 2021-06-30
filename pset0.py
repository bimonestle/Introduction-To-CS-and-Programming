# Write a program that does the following in order:
# 1. Asks user to enter a number "x"
# 2. Asks user to enter a number "y"
# 3. Prints out number "x", raised to the power "y"
# 4. Prints out the log (base 2) of "x"

import numpy as np

numbX = int(input("Enter a number x:"))
numbY = int(input("Enter a number y:"))
powerNumb = numbX ** numbY
print("x**y:", powerNumb)
print("log(x)", np.log2(numbX))