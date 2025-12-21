# FACTORIAL

n = int(input("Enter the number :- "))
fact=1
for i in range(1,n+1):
    fact*=i
print(fact)


def fact():
    pro = 1
    n = int(input("\nEnter the number :- "))
    if n < 0:
        print("\nInvalid Input.....")
    else:
        for i in range(1, n + 1):
            pro *= i
        print("\nThe FACTORIAL is :- ", pro)
