maps = {("0", "0"), ("1", "1"), ("6", "9"), ("8", "8"), ("9", "6")}

def rotatenum(nums:str):
    left = 0
    right = len(nums)-1
    
    while(left<=right):
        print(nums[left])
        print(nums[right])
        if (nums[left],nums[right]) not in maps:
            return False
        else:
            left = left + 1
            right = right -1
    return True

print(rotatenum("169"))
