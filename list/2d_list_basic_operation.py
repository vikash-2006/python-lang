# checking the element found in list

li = [[1,2,3],[4,5,6],[7,8,9]]
for i in range(len(li)):
    for j in range(len(li)):
        print(li[i][j])
        if li[i][j] == 7:
            print(i , j )

# ===========================================================================

# sum

li = [[1,2,3],[4,5,6],[7,8,9]]
sum = 0
for i in range(len(li)):
    for j in range(len(li)):
        sum+=li[i][j]
print(sum)

# ===========================================================================

#  largest number

li = [[1,2,3],[4,5,6],[7,8,9,64]]
lar = 0
for i in range(len(li)):
    for j in range(len(li)):
        if lar < li[i][j]:
            lar = li[i][j]

print("Maximum element :- ",lar)

# ===========================================================================

# flat list 2d list into 1 list

li = [[1,2,3],[4,5,6],[7,8,9]]
l1=[]
for i in range(len(li)):
    l1.extend(li[i])
print(l1)

# ===========================================================================

# seperate out the odd number and even number from the 2d list

li = [[1,2,3],[4,5,6],[7,8,9]]
even=[]
odd =[]
for i in range(len(li)):
    for j in range(len(li)):
        if li[i][j] % 2 == 0:
            even.append(li[i][j]) 
        else:
            odd.append(li[i][j]) 
print("even :- ",even)
print("odd :- ",odd)

# ===========================================================================

# diagnol sum

li = [[1,2,3],[4,5,6],[7,8,9]]

sum = 0
for i in range(len(li)):
    for j in range(len(li[i])):
        if i == j:
            sum+=li[i][j]
print(sum)

# ===========================================================================
# reverse

li = [[1,2,3],[4,5,6],[7,8,9]]

for i in range(len(li)):
    li[i] = li[i][::-1]
print(li)

# ===========================================================================

# largest element in each row

li = [[1,2,3],[4,5,6],[7,8,9]]

for i in range(len(li)):
    a = max(li[i])
    print(a)

# ===========================================================================

# largest element in each column

li = [[2,9,5],[5,7,4],[2,6,8]]
for i in range(len(li)):
    max = 0 
    for j in range(len(li[i])):
        if li[j][i] > max:
            max = li[j][i]
    print(max)

# ==========================================================================
# transpose of list

li = [[1,2,3],[4,5,6],[7,8,9]]
transposed = []
for i in  range(len(li)):
    row=[]
    for j in range(len(li[i])):
        row.append(li[j][i])
    transposed.append(row)
print(transposed)