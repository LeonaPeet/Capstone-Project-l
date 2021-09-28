import math

# Design a calculator to calculate simple and compound interest on investment and monthly payment on a bond.
# Offer user to choose between investment or bond calculator.
# Add a while boolean expression to ensure only 'investment' or 'bond' is typed in.

print()
print ("Choose either 'Investment' or 'Bond' from the menu below to proceed:")
print()
print ("Investment       - to calculate the amount of interest you'll earn on interest.")
inv_bond = input(("Bond             - to calculate the amount you'll have to pay on a homeloan. \n\n" + ":"))
inv_bond = (inv_bond.lower())
print()

wrong = []
while inv_bond != "investment" and inv_bond != "bond":
        wrong.append(inv_bond)
        inv_bond = input("Please only enter either 'Investment' or 'Bond'. \n" + ":")
        inv_bond = (inv_bond.lower())
        print()

# For bond repayments ask the user for current value of property, interest rate & no. months for bond repayments.
# Bond formulae is: (i * v) / (1 - (1 + i)** (-m))
# v = value of current home, i = current monthly interest rate and m = no. of months
# use if statement.

if inv_bond == "bond":
    v = float(input("What is the value of your current home? \n" + "R"))
    print()
    i = float(input("What is the interest rate on your current bond? \n" + "% = "))
    i = float(i / 100 / 12)
    print()
    m = int(input("Over how many months would you like to repay the bond? \n"))
    bond = (i * v) / (1 - (1 + i)** (-m))
    bond = round(bond, 2)
    print()
    print ("Your monthly bond repayments over " + str(m) + " months will be R" + str(bond) + ".")
    print()

# For investment return ask the user for investment amount, interest rate and no. of years.
# Ask user if they would like to see simple or compound interest calculations.
# Add a while boolean expression to ensure only 'simple' or 'compound' is typed in.
# Simple interest formulae: p * (1 + r * t)
# Compound interest formulae: p * math.pow((1 + r),t))
# p = initial investment amount, r = interest, t = no. of months.
# Use if_elif statement.

if inv_bond == "investment":
    p = float(input("How much would you like to invest? \n" + "R"))
    print()
    r = float(input("What interest rate would you like to see a return on? \n" + "% = "))
    r = float(r / 100)
    print()
    t = int(input("How many years would you like to invest over? \n"))
    print()
    interest = input("Would you like to calculate 'Simple' or 'Compound' interest? \n")
    interest = (interest.lower())
    print()

    wrong = []
    while interest != "simple" and interest != "compound":
        wrong.append(interest)
        interest = input("Please only enter either 'Simple' or 'Compound'. \n" + ":").lower()
        print()

    simple_i = (p * (1 + r * t))
    simple_i = round(simple_i, 2)
    compound_i = (p * math.pow((1 + r),t))
    compound_i = round(compound_i, 2)
    
    if interest == "simple":
        print ("Your investment return over " + str(t) + " years will be R" + str(simple_i) + ".")
        print()
    
    elif interest == "compound":
        print ("Your investment return over " + str(t) + " years will be R" + str(compound_i) + ".")
        print()
