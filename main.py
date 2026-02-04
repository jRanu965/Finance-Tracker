"""FINANCE TRACKER"""

# Ask for monthly allowance
allowance = float(input("Enter your monthly allowance ($): "))

# Ask for expenses
food = float(input("How much did you spend on food? ($): "))
entertainment = float(input("How much did you spend on entertainment? ($): "))
transportation = float(input("How much did you spend on transportation? ($): "))
Other = float(input("How much did you spend on Other? ($): "))

# Calculate total expenses
total_expenses = food + entertainment + transportation + Other

# Calculate remaining balance
balance = allowance - total_expenses

# Display results
print("\n--- Monthly Summary ---")
print("Total expenses: $", total_expenses)
print("Remaining balance: $", balance)

# Conditional message based on balance
if balance > 0:
    print("Nice work! You stayed within your budget this month.")
elif balance == 0:
    print("Perfect balance! You spent exactly what you had.")
else:
       print("Failed booooooooooo!!!!!!!!")