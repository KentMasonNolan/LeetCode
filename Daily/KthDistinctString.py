class Solution(object):
    def kthDistinct(self, arr, k):

        my_dict = {}
        for key in arr:
            if key not in my_dict:
                my_dict[key] = 1
            else:
                my_dict[key] += 1

        distinct_strings = []
        for key in arr:
            if my_dict[key] == 1:
                distinct_strings.append(key)

        if len(distinct_strings) >= k:
            return distinct_strings[k-1]
        else:
            return -1

        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """

sol = Solution()
print(sol.kthDistinct(["d","b","c","b","c","a"], 2))  # Output: "a"
print(sol.kthDistinct(["aaa","aa","a"], 1))  # Output: "aaa"
print(sol.kthDistinct(["a","b","a"], 3))  # Output: ""