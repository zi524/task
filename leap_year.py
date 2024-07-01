year_number=int(input("Enter the year?\n"))
if year_number%4==0 :
    if year_number%400==0 :
       print("it is a leap year")  
    else:
        if year_number%100==0 :
            print("it is not a leap year")
        else:
            print("it is a leap year")