# Function to print the table of a number
def print_table(number):
    print(f"Multiplication table of {number}:")
    for i in range(1, 11): 
        print(f"{number} x {i} = {number * i}")

# Taking input 
number = int(input("Enter a number: "))

# Calling the function 
print_table(number)
