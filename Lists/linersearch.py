#liner search
def liner_search(nums , target):
    for i in nums:
        if i == target:
          return True
    return False
            
print(liner_search([10, 56, 78, 90],90))

#liner search finding element index
def liner_search(nums , target):
    for i in range (len(nums)):
        if nums[i] == target:
            print(f"elemnt found at index {i}")  
        else:
            print("element not found")   
print(liner_search([10, 56, 78, 90],90))

#reverse the array
def rev_array(nums):
    reverse = []
    for i in range (len(nums)):
        reverse.insert(0, nums[i])
    print(reverse)
    
rev_array([1,2,3,4,5])