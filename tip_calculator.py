# I've created a very simple calculator that helps friends split the bill.
# It will ask for the total amount of the bill, the percentage of tip you want to apply and it will
# ask how many people will split the bill. I've rounded the result to 2 digits after the floating point.

print('Welcome to the tip calculator.')
bill = float(input('What was the total bill? $'))
tip = int(input('Whate percentage tip would you like to give? 10, 12, or 15? '))
people = int(input('How many people to split the bill? '))

each_to_pay = round((bill + (bill * (tip / 100))) / people, 2)

print(f'Each person should pay: ${each_to_pay}, tips included.')