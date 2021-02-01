strs = ["flower","plow","flight"]

def common_chars(strs:list):
    shortest = min(strs,key = len)
    
    for i,v in enumerate(shortest):
        for words in strs:
            if words[i] != v:
                return words[:i]
            else:
                return shortest

print(common_chars(strs))

for i in xrange(strs):
    print(i)
            