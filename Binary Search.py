nums = [-1,0,3,5,9,12]
target = 19
Output: 4

class solution:
    def binarySearch(self, nums : list, target : int):
        left = 0
        right = len(nums)-1
        mid = 0
        
        while left < right:
            mid = (left + right)//2
            if nums[mid] < target :
                left = mid + 1
            elif nums[mid] > target:
                right = mid -1
            else:
                return mid
        return -1
        
s = solution()
print(s.binarySearch(nums,target)) 
    