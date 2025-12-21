def fact():
    pro = 1
    n = int(input("\nEnter the number :- "))
    if n < 0:
        print("\nInvalid Input.....")
    else:
        for i in range(1, n + 1):
            pro *= i
        print("\nThe FACTORIAL is :- ", pro)


def prime():
    n = int(input("\nEnter the number :- "))
    if n < 0:
        print("\nInvalid input........")
    else:
        count = 0
        for i in range(2, n // 2 + 1):
            if n % i == 0:
                count = 1
                break
        if count == 0:
            print("\n", n, "is PRIME number.....")
        else:
            print("\n", n, "is not PRIME number.....")


def even():
    n = int(input("\nEnter the number :- "))
    if n < 1:
        print("\nThis is not valid....")
    else:
        if n % 2 == 0:
            print("\n", n, "is EVEN number.....")
        else:
            print("\n", n, "is ODD number......")


print("\n*********** MENU DRIVEN **********")
print("Press 1 for check EVEN/ODD ")
print("Press 2 for check PRIME ")
print("Press 3 for find FACTORIAL ")
print("Press 4 for EXIT ")

ch = int(input("\nEnter the choice :- "))

if ch == 1:
    even()
elif ch == 2:
    prime()
elif ch == 3:
    fact()
elif ch == 4:
    exit()
else:
    print("Invalid Input...")
