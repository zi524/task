def get_length(number):
    i=0
    while number!=0:
        number=int(number/10)
        i=i+1
    return i
def sum_digits(number,length):
    out=0
    i=0
    array=[]
    for j in range(length):
        x=number%10
        array.append(int(x))
        number=int(number/10)
    for i in range(length):
        out=out+array[i]
    return out            
if __name__ == "__main__":        
    numbeer=int(input("Enter number\n"))
    length=get_length(numbeer)
    out=sum_digits(numbeer,length)
    print(out)
    