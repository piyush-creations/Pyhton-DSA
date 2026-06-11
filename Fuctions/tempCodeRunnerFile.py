def factorial_n(num):
    factorial = 1
    while(num > 0 ):
        factorial = num * (num -1 )
        num -=1
    return factorial
a = factorial_n(5)
print(a)