intrvlsa = [[1,3],[2,6],[8,10],[15,18]]

def merge_intrvls(intrvls):
    start = 0
    end = 1
    intrvls.sort(key = lambda x : x[0])
    left = 0
    
    for left in range(1,len(intrvls)-1):
        if intrvls[left-1][end] < intrvls[left][start]:
            left = left + 1
        elif intrvls[left-1][end] >= intrvls[left][start]:
            intrvls[left-1] = [intrvls[left-1][start],intrvls[left][end]]
            intrvls.pop(left)
            left = left + 1
    
    return intrvls

print(merge_intrvls(intrvlsa))