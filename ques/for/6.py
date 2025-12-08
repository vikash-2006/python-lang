n = int(input("Enter numbers for Fibonacci :-  "))
a, b = 0, 1

if n <= 0:
    print("Please enter a positive number")
elif n == 1:
    print("Fibonacci Series:", a)
else:
    print("Fibonacci Series:", end=" ")
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
