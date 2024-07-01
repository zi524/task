def rem(number,n):
    remind=number%n
    new=number-remind
    return remind
def converter(number,n):
    out=0
    i=0
    while number!=0:
        reminder=rem(number,n)
        out=out+(reminder*int(pow(10,i)))
        number=int(number/2)
        i=i+1
    return out            
if __name__ == "__main__":        
    numbeer=int(input("Enter number\n"))
    base=int(input("Enter base number \n"))
    out=converter(numbeer,base)
    print(out)
    