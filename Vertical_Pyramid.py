# Output:
"""
*
**
***
****
*****
******
*****
****
***
**
*
"""



n=eval(input("Enter the no. of row: "))
for i in range(1,n+1):
    print("*"*i)

for i in  range(n,-1,-1):
    print("*"*i)
