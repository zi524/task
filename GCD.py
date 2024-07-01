a=int(input("Enter first no"))
b=int(input("Enter secound no"))
temp1=[]
temp2=[]
finish=0
#first number divisors
for i in range(a+1):
    if i>0:
        if a%i==0 :
            temp1.append(i)
print(temp1)
#secound number divisors             
for j in range(b+1):
    if j>0:
        if b%j==0 :
            temp2.append(j)  
print( temp2)
#compare
for k in range(len(temp1)-1,0,-1) :           
    for l in range(len(temp2)-1,0,-1):
        if temp1[k]==temp2[l]:
            print("GCD EQUAL ",temp1[k])
            finish=1
            break
    if finish==1:
        break    