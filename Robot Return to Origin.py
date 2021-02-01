moves = "UD"

def robotMoves(moves:list):
    mapping = {"U":[0,1],"D":[0,-1],"L":[-1,0],"R":[1,0]}
    x,y = 0,0
    for str in moves:
        x += mapping[str][0]
        y += mapping[str][1]
    
    return ((x==0) and (y==0))

print(robotMoves(moves))