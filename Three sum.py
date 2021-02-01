nums = [9,1,2,8,5,7]
target = 12

def sum3(nums : list, target : int):
    nums.sort()
    print(nums)
    ans = {}
    i = 0
    left = i+1
    right = len(nums)-1
    
    while left <= right:
        temp = nums[i] + nums[left] + nums[right]
        
        if temp == target :
            ans[i] = [nums[i] , nums[left] , nums[right]]
        if temp < target:
            left += 1
        if temp > target:
            right -= 1 
        i = i + 1   
    return ans

print(sum3(nums,target))    