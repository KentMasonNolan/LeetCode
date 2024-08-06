def removeElement(nums, val):
    elements = 0
    new_nums = []
    for i in range(len(nums)):
        if nums[i] != val:
            elements += 1
            new_nums.append(nums[i])
    return new_nums

nums = [3,2,2,3]
val = 3

print(removeElement(nums, val))