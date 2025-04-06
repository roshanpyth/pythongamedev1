matrix=[ [1,2,3],
         [4,5,6],
         [7,8,9] ]
print(matrix)
print(len(matrix))
print(matrix[1][1])
#when you want to get a specific number identify the row and the number within the row
print(matrix[2][2])

for i in  range (len(matrix)):
    for j in range (len(matrix[i])):
        print(matrix[i][j],end=" ")
    print("\n")

