# Distance Between Two Point:

x1=eval(input("Enter the value of x1: "))
y1=eval(input("Enter the value of y1: "))
x2=eval(input("Enter the value of x2: "))
y2=eval(input("Enter the value of y2: "))

dis_=((x2-x1)**2 +(y2-y1)**2)**0.5

print(f"The Distance B/w ({x1},{y1}) and ({x2},{y2}): {dis_} unit")
