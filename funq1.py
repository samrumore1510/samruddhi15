# Function to calculate factorial
def factorial(n):
    # Base case: 
    if n == 0 or n == 1:
        return 1
    
    else:
        return n * factorial(n - 1)

# Taking input 
number = int(input("Enter a number: "))

#if the number is negative
if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    # Calling 
    result = factorial(number)
    print(f"The factorial of {number} is {result}")
