grid = [10,2,34,58,78,98,34,24,87,99,90]

def bnrySrch(grid : list,target):
    grid.sort(key =  lambda x : x)
    print(grid)
    
    left,right = 0,len(grid)-1
    while(left < right):
        mid = (right-left)//2    
        if grid[mid] < target:
            right = mid - 1
        elif grid[mid] > target:
            left = mid + 1
        else:
            print("mid " + mid)
            return grid[mid]
    print(mid)    
    return grid[mid]
        
print(bnrySrch(grid,98))