A = "this apple is sweet"
B = "this apple is sour"

counter = dict()
combine = list()
ans = []

combine.extend(A.split())
combine.extend(B.split())

for word in combine:
    if word not in counter:
        counter[word] = 1
    else:
        counter[word] = int(counter.get(word)) + 1

for i in counter:
    if counter[i] == 1:
        ans.append(i)
  
print(ans)