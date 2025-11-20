# n = int(input("Enter the number of rows: "))
# for i in range(n, 0, -1):  # include 1
#     for j in range(1, n + 1):  # include n
#         if j <= i:
#             print("* ", end="")
#         else:
#             print("  ", end="")
#     print()


n = int(input("Enter the number of rows: "))
for i in range(1, n + 1):
    row_string = print("* " * i)
