###direction = {'N': (0, 1), 'S': (0, -1), 'E': (1, 0), 'W': (-1, 0)}

class cross:
    def path_cross(self,path:dict):
        curr = (0,0)
        x = 0
        y = 0
        for direction in path:
            if direction == "N":
                y = y + 1
            if direction == "S":
                y = y -1
            if direction == "E":
                x = x + 1
            if direction == "S":
                x = x -1
        if (x,y) == curr:
            return True
        else:
            return False

walk = cross()
print(walk.path_cross("NEWSW"))


