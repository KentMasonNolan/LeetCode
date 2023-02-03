strs = ["flower", "flow", "flight"]
output = ""
def longestCommonPrefix(strs):
    stop = 0

    print(list((zip(*strs))))
    for letters in zip(*strs):
        if len(set(letters)) == 1:
            stop += 1
        else:
            break

    print(strs[0][:stop])


longestCommonPrefix(strs)