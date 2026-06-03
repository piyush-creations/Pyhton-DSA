a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)

#modulus opreators
print(a%b)

#Even or Odd Example
#if else
num = int(input("Enter number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")
    
age = int(input("Enter age: "))

if age >= 18:
    print("Adult")
else:
    print("Minor")
    
#elif
marks = int(input())

if marks >= 90:
    print("A")
elif marks >= 75:
    print("B")
elif marks >= 50:
    print("C")
else:
    print("Fail")