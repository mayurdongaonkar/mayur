paragraph = ["i", "love", "leetcode", "i", "love", "coding"]

def wordcounter(paragraph):
    ans = []
    tracker = {}

    for word in paragraph:
        if word not in tracker:
            tracker[word] = 1
        else:
            tracker[word] = int(tracker.get(word)) + 1
    
    for keyValue in tracker:
        ans.append([keyValue,tracker.get(keyValue)])

    ans.sort(key = lambda x : (x[1],x[0]), reverse=True)
    
    print(ans)

wordcounter(paragraph)