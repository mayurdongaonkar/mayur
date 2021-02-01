lst = [('candy','30','100'), ('apple','10','200'), ('baby','20','300')]
lst.sort(key=lambda x:x[1])
print(lst)

nums = [1,1,2,2,2,3]
from collections import Counter
d = Counter(nums)
print(d)
print(nums.sort())
print(nums.sort(key = lambda x:d[x]))
print(nums)

from collections import deque
d = deque(nums)
d.append(4)
print(d[0])


for i in d:
    print(i)
    