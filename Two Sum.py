nums = [2,7,11,15]
target = 9
seen = dict()
    
for (index,key) in (enumerate(nums)):
    ##print(index,key)

    remaining = target - nums[index]
    if remaining not in seen:
        seen[key] = index
    else:
        print("1")
        print(seen[remaining],index)