text = "lettcode"

class solutions:
    def FrstUnqString(self, text : str):
        counter = {}
        first_non_unique = list()
        for letter in text:
            if letter not in counter:
                counter[letter] = 1
            else:
                if len(first_non_unique) == 0:
                    first_non_unique.append(letter)
                    ans = text.index(letter)
              
                counter[letter] = int(counter[letter]) + 1
        
        print(counter)
        print(ans)

        if max(counter.values()) > 1:
            return (ans)
        else:
            return (-1)

ans = solutions()
print(ans.FrstUnqString(text))