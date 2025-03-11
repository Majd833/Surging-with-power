def power2(number):
    if (number==0):
        return 0
    if ((number&(~(number-1)))==number):
        return 1
    return 0
number=int(input("Enter the number:"))
if (power2(number)):
    print("the number is a power of 2")
else:
    print("The number isn't a power of 2")