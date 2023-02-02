s = 'III'



def romanToInt(s):
    romanInt = 0
    romanArray = list(s)

    for i in romanArray:
        if i == 'I':
            romanInt += 1
            print(i)
        else:
            romanInt += 1
        if i == 'V':
            romanInt += 5
        if i == 'X':
            romanInt += 10
        if i == 'L':
            romanInt += 50

    print(romanInt)

romanToInt(s)