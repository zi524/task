
def factorial(self):
    ans=1
    while self!=0:
        ans*=self
        self=self-1
    return ans
if __name__ == "__main__":
    a=int(input("number\n"))
    if a<=12:
        ans=factorial(a)
        print("factorial=",ans)
    else:
        print("factorial is not possible")