def rev_array(nums):
    reverse = []
    for i in range (len(nums)):
        reverse.insert(0, nums[i])
    print(reverse)
    
rev_array([1,2,3,4,5])