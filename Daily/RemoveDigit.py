def removeDigit(number, digit):
    array_digits = [int(digit) for digit in str(number)]

    array_digits.remove(int(digit))

    result_string = ''.join(map(str, array_digits))

    print(result_string)
    return result_string


removeDigit("551", 5)
