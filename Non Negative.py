def countNegatives(grid):
    List = list()
    ans  = 0

    for i in grid:
        List += i

    for i in List:
        if i < 0:
            ans += 1
        else:
            ans += 0
    
    return ans

grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]

print(countNegatives(grid))