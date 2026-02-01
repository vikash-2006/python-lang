n = 5
for i in range(n):

    # Printing the spaces
    for j in range(i+1):
        print(' ', end=' ')

    # Printing the alphabets
    for j in range(2*(n - i) - 1):
        print(chr(65 + j), end=' ')
    print()


for i in range(1,n):

    # Printing spaces (decreasing)
    for j in range(n - i):
        print(' ', end=' ')

    # Printing alphabets (increasing)
    for j in range(2*i + 1):
        print(chr(65 + j), end=' ')
    print()
