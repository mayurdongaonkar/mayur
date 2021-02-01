heights        = [1,1,4,2,1,3]
heights_sorted = sorted(heights,reverse=True)
x = 0

for i in range(0,len(heights)-1):
    if heights[i] != heights_sorted[i] :
        x = x + 1

print(x)