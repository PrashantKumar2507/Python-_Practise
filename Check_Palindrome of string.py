# Check the is paindrome or not
ch = input("Enter the string : ")

st= ch[::-1]
print(f"The sring is : {st}")

if st==1:
    print(f"{st} is Palindrome.")
else:
    print(f"{st} is not Palindrome.")
