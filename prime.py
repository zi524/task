import math

number=int(input("Enter the number"))
if number>1:
    if number==2:
        print("It is a prime number")
    elif number%2!=0 :
        sqrt_n = int(math.sqrt(number)) + 1
        for i in range(3, sqrt_n, 2):  # Iterate through odd numbers from 3 to sqrt_n
            if number % i != 0:
                 print("It is a prime number")
            else:
                 print("It is not a prime number")      