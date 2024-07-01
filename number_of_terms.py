import math
def factorial(self):
    ans=1
    while self!=0:
        ans*=self
        self=self-1
    return ans
if __name__ == "__main__":
    x=int(input("number\n"))
    ans=math.sin(x)
    parity=-1
    m=0
    for i in range(1,30,2):
        parity=parity*-1
        ans=ans-(parity*(int(pow(x,i))/factorial(i)))
        m=m+1  
        if ans<=0:
            break
    print("number=",m)      