def PhoneLetterConbination(input):

    mapping = {
                '1' : 'abc',
                '2' : 'def',
                '3' : 'ghi',
                '4' : 'jkl',
                '5' : 'mno',
                '6' : 'pqr',
                '7' : 'stu',
                '8' : 'wxyz',
                '9' :  '',
                '0' : ''
            }    
    
    answer_combine = [' ']

    for digit in input:
        current_combine = list()
        for letter in mapping[digit]:
    
            for c1 in answer_combine:
                current_combine.append(c1 + letter)

        answer_combine.append(current_combine)
    return answer_combine

print(PhoneLetterConbination('23'))


