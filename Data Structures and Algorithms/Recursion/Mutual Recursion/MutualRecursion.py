# Mutual Recursion
# Two functions are called mutually recursive if the first
# function makes a recursive call to the second function and the second function,
# in turn, calls the first one.

def isEven(num):
    if num == 0:
        return True
    else:
        return isOdd(num - 1)

def isOdd(num):
    if num == 0:
        return False
    else:
        return isEven(num - 1)


number = int(input("Enter a number: "))
if isEven(number):
    print(f"{number} is an even number.")
else:
    print(f"{number} is an odd number.")