dict_emp = [[1,4],[2,4],[3,4],[4,5],[6,5]]
emp = [4,5,{4}]


def manger_reporting(dict_emp,emp):
    ans = []
    
    for manger in range(len(emp)):
        for counter in range(0,len(dict_emp)-1):
            if emp[manger] == dict_emp[counter][1]:
                    ans.append(dict_emp[counter][0])
    return ans

print(manger_reporting(dict_emp,emp))