nums = [2,0,2,1,1,0]

def sortColors(nums):
    beg, mid, end = 0, 0, len(nums) - 1
        
    while mid <= end:
            if nums[mid] == 0:
                nums[beg], nums[mid] = nums[mid], nums[beg]
                mid += 1
                beg += 1
            elif nums[mid] == 2:
                nums[mid], nums[end] = nums[end], nums[mid]
                end -= 1
            else:  #nums[mid] == 1:
                mid += 1
    print(nums)

sortColors(nums)