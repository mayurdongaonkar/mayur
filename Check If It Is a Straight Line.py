coordinates = [[1,2],[2,3],[3,4],[4,5],[6,8]]

def isStaitline(coordinates : list):
    coordinates.sort(key = lambda x : x[0])
    size = len(coordinates)
    x,y = 0,1
    flag = 0
    
    for counter in range(0,size-1):
        if coordinates[counter][x]+1 == coordinates[counter+1][x] and coordinates[counter][y]+1 == coordinates[counter+1][y]:
            flag += 0
        else:
            flag +=1
    
    if flag == 0: 
        return True 
    else: 
        return False

print(isStaitline(coordinates))