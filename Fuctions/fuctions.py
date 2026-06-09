#introduction to function 
def greet(name):
    print("Hello, " + name + ". How are you?")
greet("piyush")

#function with parameters
def add(a, b):
    return a + b
result = add(5, 3)
print("The sum is:", result)

#function with default parameters
def greet(name="Guest"):
    print("Hello, " + name + ". How are you?")
greet()
greet("piyush")

#even odd function 
def is_even(num ):
    if num % 2 == 0:
        return True
    else:
        return False
number = int(input("Enter a number: "))

