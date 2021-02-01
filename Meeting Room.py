ip_grid = [[0, 30],[5, 10],[15, 20],[6,10]]

def min_meetrooms(grid):
    print(grid)
    curr = 0

    start = 0
    end = 1

    ans = 0

    grid.sort(key = lambda x : x[0])

    print(grid)

    for curr in range(0,len(grid)-1):
        if grid[curr-1][end] > grid[curr][start]:
            ans += 1
        else:
            ans += 0
    return ans

print(min_meetrooms(ip_grid))
        
    
