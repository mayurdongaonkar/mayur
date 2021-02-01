def letterCombinations(digits):
    interpret_digit = {
            '1': '',
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
            '0': ' '}

    if digits:
        all_combinations = [''] 
    else:
        []

    for digit in digits:
            current_combinations = list()
            for letter in interpret_digit[digit]:
                for combination in all_combinations:
                    current_combinations.append(combination + letter)
            all_combinations = current_combinations
        
    return all_combinations

print(letterCombinations('23'))


all_combination = '123'
for letter in 'abc':
    for combination in all_combination:
        print(combination + letter)
