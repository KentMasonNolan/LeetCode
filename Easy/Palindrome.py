import math


class Solution(object):
    def isPalindrome(self, s):
        halfValueLength = math.trunc(len(str(s))/2)
        i = 0
        j = len(str(s)) - 1
        x_array = [int(t) for t in str(s)]
        if s <= 0:
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

