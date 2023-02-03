s = "()))"

def isValid(s):
    for i in range(len(s)):
        print(s[i])
        if s[i] == '(' and s[i+1] == ')':
            print('true')
            return True
        else:
            print('false')
            return False

isValid(s)