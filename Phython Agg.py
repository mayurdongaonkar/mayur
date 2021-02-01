grid = [[1,"Mayur",100],[1,"Sonal",200],[1,"Shreya",300],[2,"Shreya",800],[2,"Avni",1800],[3,"Chamu",18000]]

#### Tell me department id who is paying maximum aggregated salary.

def deptMaxSal(grid : list):
    group = dict()
    result = list()
    for item in grid:
        if item[0] not in group:
            group[item[0]] = item[2]
        else:
            group[item[0]] = item[2] + int(group[item[0]])
    
    for key,value in group.items():
        result.append([key,value])
    
    print(sorted(group.items(),key= lambda x : x[1],reverse = True))
    
    result.sort(key = lambda x : x[1], reverse= True)
    return result[0][0]

print(deptMaxSal(grid))