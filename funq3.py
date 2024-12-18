# Function to check if a person can vote
def can_vote(age):
    # The voting age is 18 or above
    if age >= 18:
        return True
    else:
        return False

# Taking input 
age = int(input("Enter your age: "))

# Checking if the person can vote
if can_vote(age):
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
