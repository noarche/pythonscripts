# Prompt the user for the first number
num1 = input("Enter the water bill amount: ")

# Prompt the user for the second number
num2 = input("Enter the electric bill amount: ")

# Convert the user input from string to float
num1 = float(num1)
num2 = float(num2)

# Add the numbers and store the result in a variable
result = num1 + num2

# Multiply the result by 0.33 and store the final result in a variable
final_result = result * 0.33

# Print the final result
print(final_result)