n = int(input("Enter the number :- "))

# Upper part
for i in range(n, 0, -1):
    for j in range(n, 0, -1):
        if j < i:
            print("* ", end=" ")   # changed here
        else:
            print("  ", end=" ")   # changed here
    print()

# Lower part
for i in range(2+1, n + 1):          # this already removes the blank line
    for j in range(n, 0, -1):
        if j < i:
            print("* ", end=" ")   # changed here
        else:
            print("  ", end=" ")   # changed here
    print()
