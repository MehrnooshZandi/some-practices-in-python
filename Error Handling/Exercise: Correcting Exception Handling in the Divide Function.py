'''
Examine the following code and troubleshoot it.

Goal: This function should take two numbers and return the division value, but handle it properly if there is a problem.

def divide(a, b):
result = a / b
return result

num1 = int(input("Enter first number: "))

num2 = int(input("Enter second number: "))

print("Result:", divide(num1, num2))

Your tasks:

This code will throw a ZeroDivisionError if num2 = 0. Handle this error.
If the user enters a non-numeric value (for example, hello), a ValueError will be thrown. Handle this error.
After the function executes, display a message saying "The program ran successfully!", even if an error occurs.
The program should not crash! Instead, it should prompt the user for valid input.
'''
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return None

while True:
    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        result = divide(num1, num2)
        if result is not None:
            print("Result:", result)
        break  # Exit loop if everything was successful
    except ValueError:
        print("Error: Please enter a valid integer.")

finally:
    print("The program ran successfully!")
