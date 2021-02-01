nums = [1,1,1,2,2,2,3,0]

def weight_sort(nums):
    from collections import Counter
    d = Counter(nums)
    ##nums.sort(reverse = True)
    nums.sort(key = lambda x : d[x] )
    return nums

print(weight_sort(nums))       
        