# Tail Recursion
# The function makes a recursive call as its very last operation

# Create a recursive function that will find for the factorial of a number

def factorial(num, base):
    if num <= 1:
        return base
    return factorial(num - 1, base * num)


number = int(input("Enter a number: "))
print(f"{number}! = {factorial(number, 1)}")
