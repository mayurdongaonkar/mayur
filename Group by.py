grid = [[1,"Mayur",100],[1,"Sonal",200],[1,"Shreya",300],[2,"Shreya",800]]

grid.sort(key = lambda x : x[2], reverse = True)
print(grid[1][1])

def dept_group(grid):
    ans = {}
    for i in grid:
        if i[0] not in ans:
            ans[i[0]] = i[2]
        else:
            ans[i[0]] = int(ans.get(i[0])) + i[2]

    high = []
    for i in ans:
        high.append([i,ans[i]])
    high.sort(key = lambda x : x[1],reverse = True)

    return ans,high[1]

print(dept_group(grid))