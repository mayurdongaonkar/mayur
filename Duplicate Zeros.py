nums = [1,0,2,0,3]
opts = [1,0,0,2,0,0,3]

def duplicate_zeros(nums):
    temp = []
    for item in nums:
        temp.append(item)
        if item == 0:
            temp.append(item)
    
    for i in range(len(nums)):
        nums[i] = temp[i]
        
    return nums

print(duplicate_zeros(nums))

