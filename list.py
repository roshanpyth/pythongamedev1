matrix=[ [1,2,3],
         [4,5,6],
         [7,8,9] ]
print(matrix)
print(len(matrix))
print(matrix[1][1])
#when you want to get a specific number identify the row and the number within the row
print(matrix[2][2])
print(matrix[2][0])
#first one is the main row then 2nd is the individual integer


for i in  range (len(matrix)):
    for j in range (len(matrix[i])):
        print(matrix[i][j],end=" ")
    print("\n")

row=int(input("How many rows would you like"))
column=int(input("How many columns would you like"))
list=[]

for i in range(row):
    tem=[]
    for j in range(column):
        element=int(input("Enter the value"))
        tem.append(element)
    list.append(tem)

for i in range(len(list)):
    for j in range(len(list[i])):
        print(list[i][j],end=" ")
    print("\n")

metricsA=[[1,2],
          [3,4]]

MetricsB=[[4,2],
          [5,6]]
result=[[0,0],[0,0]]

for i in range(2):
    for j in range(2):
        result[i][j]=metricsA[i][j]+MetricsB[i][j]