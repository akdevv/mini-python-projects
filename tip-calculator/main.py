print("Welcome to the tip calculator.")

# Take input of bill amount, percentage of tip and number of people
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

# Calculations
total_bill = bill + (tip / 100 * bill)
bill_per_person = round((total_bill / people), 2)

# Print result
print(f"Each person should pay: ${bill_per_person}")