#for loop
for i in range(5):
    print(i)
#understanding Range function
for i in range(2,10):
    print(i)
#step size
for i in range(2,10,2):#step size of 2
    print(i)
#while loop
i = 1

while i <= 5:
    print(i)
    i += 1
#Sum of first n natural numbers
n = int(input())
sum = 0

for i in range(1, n + 1):
    sum += i

print(sum)
#Count digits
n = int(input("Enter number:"))
count = 0
while n>0:
    n = n//10
    count += 1
print(count)