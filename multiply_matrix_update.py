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
def multiply(rows,cols,rows2,cols2,mat1,mat2):
    mult=matrix_intialize_by_zeros(rows,cols2)
    if cols==rows2:
        for i in range(rows):
            for j in range(cols2):
                for k in range(cols):
                    mult[i][j]+=mat1[i][k]*mat2[k][j]
    return mult    
if __name__ == "__main__":
    rows = int(input("Enter the number of rows first matrix: "))
    cols = int(input("Enter the number of columns: first matrix: "))
    matrix1=matrix_intialize(rows,cols)
    rows2 = int(input("Enter the number of rows secound matrix: "))
    cols2 = int(input("Enter the number of columns secound matrix: "))
    matrix2=matrix_intialize(rows2,cols2)
    multiple=multiply(rows,cols,rows2,cols2,matrix1,matrix2)
    print(multiple)