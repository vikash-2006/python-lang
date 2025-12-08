n = int(input("Enter a number: "))
if n >= 1:
    if n % 2 == 0:
        print(n, "is even")
    else:
        print(n, "is odd")
elif n < 0:
    print("Negative number")
else:
    print(" Zero")