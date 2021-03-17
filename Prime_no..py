# Prime No.

num = eval(input("Enter the no. : "))

for i in range (2,num):
    if(num%i==0):
        print (f"NO! , {num} is prime no. ")
        break
else :
    print (f"Yes , {num} is prime no. ")
