import math

x = int(input("Enter your value: "))

def isPalindrome(x):
    halfValueLength = math.trunc(len(str(x))/2)
    i = 0
    j = len(str(x)) - 1
    x_array = [int(t) for t in str(x)]
    if x <= 0:
        print("False")
        return False
    while i <= halfValueLength:
        if x_array[i] != x_array[j]:
            print("False")
            return False
        else:
            i += 1
            j -= 1
    print("True")
    return True

isPalindrome(x)
