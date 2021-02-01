moves = "UDLRU"

def judgeCircle(moves : str):
    map = dict()
    map = {'R':[1,0],'L':[-1,0],'U':[0,1],'D':[0,-1]}
    
    x,y = 0,0
    
    for move in moves:
        x += map[move][0]
        y += map[move][1]
    
    return (x == 0) and (y==0)
    
print(judgeCircle(moves))