nums = [-1,0,3,5,9,12]
target = 9

class solution:
    def search_digit(self, nums:list,target : int):
        if not nums:
            return -1
        elif target in nums:
            return nums.index(target)
        else:
            return -1
        
s = solution()
print(s.search_digit(nums,target))