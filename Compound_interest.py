p=eval(input("Enter the Principle : "))
r=eval(input("Enter the annual interest rate: "))
n=eval(input("Enter the no. of time : "))
t=eval(input("Enter the time the money is invested for: "))

r/=100
ci = (p*(1+r/n)**(n*t))-p
print(f"The compound interest is : {ci}")
