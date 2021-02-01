##rec1 = [0,0,2,2] 
##rec2 = [1,1,3,3]

rec1 = [0,0,1,1]
rec2 = [1,0,2,1]

def isoverlpap(rec1 : list, rec2 : list):
    left    =   max(rec1[0],rec2[0])
    right   =   min(rec2[3],rec2[3])
    bottom  =   max(rec1[1],rec2[1])
    top     =   min(rec1[3],rec2[3])
    
    if (left < right and bottom < top):
        return True
    else:
        return False

print(isoverlpap(rec1,rec2))