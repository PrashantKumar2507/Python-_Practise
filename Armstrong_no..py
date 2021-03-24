# Armstrong

n=eval(input("Enter the no. :"))
d=0
sum=0
n1=n
while n!=0:
                d=n%10
                sum=sum+d*d*d
                n//=10
if n1==sum:
                print("Armstrong no . ")
else:
                print("Not Armstrong no.")
