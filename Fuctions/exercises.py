#sum of first n numbers
def sum_of(num):
    sum = 0
    while(num > 0 ):
        sum = sum + num 
        num= num - 1
    return sum

a = sum_of(5)
print(a)

#factorial of number 
def factorial_n(num):
    factorial = 1
    while(num > 0 ):
        factorial =factorial * num 
        num -=1
    return factorial
a = factorial_n(5)
print(a)

#count digits
def count_digits(n):
    count = 0

    while n > 0:
        n = n // 10
        count += 1

    return count

print(count_digits(12345))
