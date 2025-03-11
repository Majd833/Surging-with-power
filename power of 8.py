def power8(number):
    bitpos=0
    mask=1
    while bitpos<=63:
        mask<<=bitpos
        if mask==number:
            return True
        bitpos+=3
        mask=1
    return False
number=int(input("Enter your number:"))
if (power8(number)):
    print(number,"is a power of 8")
else:
    print(number,"isn't a power of 8")