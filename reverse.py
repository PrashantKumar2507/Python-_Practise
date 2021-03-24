# reverse of digit

n= eval(input("Enter the no."))
d=0
rev=0
while n!=0:
                d=n%10
                rev=rev*10+d
                n//=10
print(rev)
