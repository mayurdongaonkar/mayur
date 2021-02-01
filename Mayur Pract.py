l = [[1,2],[3,4],[5,6]]
o = [4,5]

def inslist(l,o):
        i = 0
        res = []

        while i < len(l) and o[0] > l[i][0]:
                res.append(o)
                i += 1
        return res

print(inslist(l,o))


                        
                        
