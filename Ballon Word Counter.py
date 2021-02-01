class solutions:
    def word_count(self, text : str):
        mapping = {"b": 0, "a":0, "l":0 }
        for letter in text:
            if letter in (mapping):
                mapping[letter] += 1
        return min(mapping.values())

sol = solutions()
print(sol.word_count("ballab"))