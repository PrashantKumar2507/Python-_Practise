n =eval(input('Enter the raw : '))
ch=65
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(ch),end=" ")
        ch+=1
    print()

#Output:
"""
A
B C
D E F
G H I J
K L M N O
P Q R S T U
V W X Y Z [ \
"""
