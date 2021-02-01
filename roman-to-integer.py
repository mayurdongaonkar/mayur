mapping = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}

input = 'MDCLXIV'

class solutions:
    def romanConv(self, mapping : dict, input : str):
        total = 0
        for i in range(0,len(input)-1):
            print(input[i])
            if mapping[input[i]] < mapping[input[i+1]]:
                total += mapping[input[i+1]] - mapping[input[i]]
            else:
                total += mapping[input[i]]
                print(total)
        return total

s1 = solutions()
print(s1.romanConv(mapping,input))