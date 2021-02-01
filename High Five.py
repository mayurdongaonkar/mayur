items = [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]

def highFive(items : list):
    grouping = dict()
    for itm in items:
        if itm[0] not in grouping:
            grouping[itm[0]] = [itm[1]]
        else:
            grouping[itm[0]].append(itm[1])

    for i in grouping:
        grouping[i].sort(reverse=True)
        grouping[i] = grouping[i][0:5]
        grouping[i] = sum(grouping[i])//5

    return grouping

print(highFive(items))