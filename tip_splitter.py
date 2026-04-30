"""
Jeremy Eldredge
IS 303 - A01

Tip Splitter
This program calculates the amount of tip each person should pay when splitting a bill. The user is prompted to enter the total bill amount, the percentage they would like to tip, and the number of people sharing the bill. The program then calculates and displays the tip amount per person and the total amount each person should pay.

Inputs:
- Restaurant name
- Total bill amount
- Tip percentage
- Number of people sharing the bill

Processes:
- Calculate tip amount
- Calculate total amount per person

Outputs:
- Restaurant name
- Total bill amount
- Tip percentage
- Tip amount
- Total amount with tip
- Total amount per person
"""
# inputs
restaurant_name = input("Enter the restaurant name: ")
bill_amount = float(input("Enter the total bill amount: "))
tip_percentage = float(input("Enter the tip percentage you would like to give: "))
num_people = int(input("Enter the number of people sharing the bill: "))

# processes
tip_amount = bill_amount * (tip_percentage / 100)
total_with_tip = bill_amount + tip_amount
amount_per_person = total_with_tip / num_people

# outputs
print(f"\nRestaurant name: {restaurant_name}")
print(f"\nTotal bill amount: ${bill_amount:.2f}")
print(f"Tip percentage: {tip_percentage:.2f}%")
print(f"Tip amount: ${tip_amount:.2f}")
print(f"Total amount with tip: ${total_with_tip:.2f}")
print(f"Total amount per person: ${amount_per_person:.2f}")