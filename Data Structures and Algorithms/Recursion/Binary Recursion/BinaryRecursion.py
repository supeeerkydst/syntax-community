# Binary Recursion
# Occurs whenever there are two recursive calls for each non-base case

# Create a recursive function that will

def fibonacci(num):
    if num <= 1:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)


number = int(input("Enter a number greater than zero: "))
for i in range(number):
    print(f"{fibonacci(i)}, ", end="")