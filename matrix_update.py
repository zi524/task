def matrix_intialize_by_zeros(rows,cols):
    matrix=[]
    for i in range(rows):
        row=[]
        for j in range(cols):
            row.append(0)
        matrix.append(row)    
    return matrix
def matrix_intialize(rows,cols):
    matrix=[]
    for i in range(rows):
        row=[]
        for j in range(cols):
            row.append(int(input("Enter the element: ")))
        matrix.append(row)    
    return matrix
def matrix_transpose(rows,cols,matrix):   
    mtr=matrix_intialize_by_zeros(cols,rows) 
    for i in range(rows):
        for j in range(cols):
            mtr[j][i]=matrix[i][j]
    return mtr    
if __name__ == "__main__":        
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    matrix = matrix_intialize(rows,cols)
    print(matrix)
    transpose_matrix=matrix_transpose(rows,cols,matrix)
    print(transpose_matrix)  