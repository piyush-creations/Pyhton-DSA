# check positive or negative no.
a = int(input("enter a number: \n"))
if(a < 0):
    print("Negative")
elif(a > 0):
    print("positive")
else:
    print("enter a valid no.")

#largest of three number
b=int(input())
c=int(input())
d=int(input())
if(b>c and b>d):
    print(f"{b} is largest")
elif(c>d and c>b):
    print(f"{c} is largest")
elif(d>b and d>c):
    print(f"{d} is largest")

#reverse a number
num = int(input("Enter a number: "))
reverse = 0
while(num > 0):
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10
print(f"Reverse of the number is: {reverse}")

#check the number is palindrome or not 
num = int(input("Enter a number: "))
original = num 
reverse = 0
while(num > 0):
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10
if(reverse ==original):
    print("palindrome number")
else:
    print("not a palindrome number")
    