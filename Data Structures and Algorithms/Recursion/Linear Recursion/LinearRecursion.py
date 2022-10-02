# Linear Recursion
# The function calls itself once each time it is invoked

# Create a recursive function that will find for the factorial of a number

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)


# user input
number = int(input("Enter a number: "))
# function call should be done after function declaration
# using f-string to display the factorial value
print(f"{number}! = {factorial(number)}")
