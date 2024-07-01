import numpy as np
def matrix (rows,cols):
    matrix = np.zeros((rows, cols))
    for i in range(rows):
        row = list(map(int, input("Enter row {} (space-separated values): ".format(i+1)).split()))
        matrix[i] = row
    return matrix
if __name__ == "__main__":
    rows = int(input("Enter the number of rows first matrix: "))
    cols = int(input("Enter the number of columns: first matrix: "))
    matrix1=matrix(rows,cols)
    rows2 = int(input("Enter the number of rows secound matrix: "))
    cols2 = int(input("Enter the number of columns secound matrix: "))
    matrix2=matrix(rows2,cols2)
    multiple=np.dot(matrix1,matrix2)
    print(multiple)