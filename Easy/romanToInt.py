s = 'IVI'

def romanToInt(s):
    romanInt = 0
    romanArray = list(s)
    length = len(romanArray)

    for i in range(length):
        if romanArray[i] == 'I':
            romanInt += 1
        if romanArray[i] == 'V':
            romanInt += 5
        if romanArray[i] == 'X':
            romanInt += 10
        if romanArray[i] == 'L':
            romanInt += 50

    print(romanInt)

romanToInt(s)