# Finding Greater no between three no.s

num1=eval(input("Enter the value of a: "))
num2=eval(input("Enter the value of b: "))
num3=eval(input("Enter the value of c: "))

if num1>num2 and num1>num3:
    print(f"a is greater than b and c")
elif num2>num3:
    print(f"b is greater than a and b")
else:
    print("c is greater than a and b")
        
