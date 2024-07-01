import numpy as np

rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))
matrix = np.zeros((rows, cols))
for i in range(rows):
    row = list(map(int, input("Enter row {} (space-separated values): ".format(i+1)).split()))
    matrix[i] = row
print(matrix)
trans=matrix.T
print("transposed matrix is \n",trans)
  