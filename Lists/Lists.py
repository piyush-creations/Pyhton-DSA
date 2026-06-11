#A list stores multiple values in a single variable.
nums = [5, 8, 12, 20]
print(nums[1])
#updating element in list
nums = [10, 20, 30]
nums[1] = 100
print(nums)
print(len(nums))
for i in nums:
    print(i)
#append at the end
nums = [1, 2, 3]
nums.append(4)
print(nums)
nums.pop()
print(nums)
nums.insert(0,100)#two args->index and value
print(nums)
nums.remove(100)
print(nums)