a=int(input("number of elements"))
c=int(input("number of shift"))
step=[]
b=[]
for i in range(0,a,1):
    b.append(int(input(f"element number {i+1}")))
for i in range(a,0,-1):
    if c<=a and c!=0:    
        c=c-1 
        x=b.pop()
        b.insert(0,x)      
print(b)