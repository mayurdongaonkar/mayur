nums = [1,2,3]

import itertools

def permute(nums):
    return list(itertools.permutations(nums))

print(permute(nums))

print(itertools.groupby(nums))

    