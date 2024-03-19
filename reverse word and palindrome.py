str = input("Enter a String:")
newstr = ""
for i in str:
    newstr = i + newstr
print(newstr)
a = str
b = newstr
if a == b:
    print(a, "is a palindrome")
else:
    print(a, "is not a palindrome")


