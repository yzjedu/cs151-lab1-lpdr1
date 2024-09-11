# Programmers:  Lucas Podowski, Donovan Raymond
# Course:  CS151, DR. Zalalem
# Due Date: 9/18/2024
# Lab Assignment: 1
# Problem Statement: You are planning a road trip and need to
# figure out the cost for gas for your trip. You will need to know
# how many miles you will travel, the miles per gallon (MPG) of your car,
# and the cost of gas. Your program should work for any values of miles,
# MPG, and gas cost without needing to modify the code between runs.
# Data In: miles, MPG, and gas_price
# Data Out:  total_cost
# Credits: Based on test cods
# Finds the cost of travel with miles traveled, MPG, and gas cost.

# Stores miles traveled, MPG and gas price
miles = int(input('How many miles have you traveled? '))
MPG = int(input('What is your cars miles per gallon? '))
gas_price = float(input('What is your cars gas price? '))

# Finds total_cost and prints
total_cost = miles / MPG * gas_price
print(round(total_cost,2))