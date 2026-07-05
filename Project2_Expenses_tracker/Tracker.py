# Project 2: Expense Tracker
# Initialize our running total outside the loop
total = 0

print("Welcome to the Expense Tracker Program")

while True:
    user_input = input("Enter an expense amount (or type 'quit'): ")
    
    # Check if the user wants to exit
    if user_input.strip().lower() == 'quit':
        break
        
    # Catch bad inputs like words instead of numbers
    try:
        new_expense = int(user_input)
        total = total + new_expense
        print(f"Added ${new_expense} to running total.")
        
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Output the final results after exiting the loop
print("\n--- Final Report ---")
print(f"Total Expenses: ${total}.00")