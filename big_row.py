import numpy as np
def matrix (rows,cols):
    matrix = np.zeros((rows, cols))
    for i in range(rows):
        row = list(map(int, input("Enter row {} (space-separated values): ".format(i+1)).split()))
        matrix[i] = row
    return matrix        
def organized(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    x=0
    f=0
    for i in range(rows):
        if np.sum(matrix[i]) > x :
            x=np.sum(matrix[i])
            f=i
    return f                    
if __name__ == "__main__":
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    matrix=matrix(rows,cols)
    organize=organized(matrix)
    print("The row with the highest sum is ",organize+1)
    temp=matrix[0].copy()
    matrix[0]=matrix[organize].copy()
    matrix[organize]=temp
    print(matrix)