nums = [1,1,2]
##nums = []
##Output: 2 
##nums = [1,2]

def remove_dups(input : list):
    
    if not input:
        return []

    for i in range(1,len(input)-1):
        if input[i] == input[i-1]:
            input.pop(i)        
    return input

print(remove_dups(nums))

print(nums[-2:])
