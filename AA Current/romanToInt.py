s = 'III'

def romanToInt(s):
    romanInt = 0
    romanArray = list(s)

    for i in range(len(romanArray)):
        if romanArray[i] == 'I' and romanArray[i+1] == 'V':
            romanInt += 4
            break
        if romanArray[i] == 'I' and romanArray[i+1] == 'X':
            romanInt += 9
            break
        if romanArray[i] == 'X' and romanArray[i+1] == 'L':
            romanInt += 40
            i += 1
        if romanArray[i] == 'X' and romanArray[i+1] == 'C':
            romanInt += 90
            i += 1
        if romanArray[i] == 'C' and romanArray[i+1] == 'D':
            romanInt += 400
            i += 1
        if romanArray[i] == 'C' and romanArray[i+1] == 'M':
            romanInt += 900
            i += 1
        if romanArray[i] == 'I':
            romanInt += 1
        if romanArray[i] == 'V':
            romanInt += 5
        if romanArray[i] == 'X':
            romanInt += 10
        if romanArray[i] == 'L':
            romanInt += 50
        if romanArray[i] == 'C':
            romanInt += 100
        if romanArray[i] == 'D':
            romanInt += 500
        if romanArray[i] == 'M':
            romanInt += 1000

    print(romanInt)

romanToInt(s)