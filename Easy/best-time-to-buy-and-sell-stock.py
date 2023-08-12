class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        leftPointer, rightPointer = 0, 1
        maxProfit = 0

        while rightPointer != len(prices):
            if prices[rightPointer] - prices[leftPointer] > maxProfit:
                maxProfit = prices[rightPointer] - prices[leftPointer]
            if prices[rightPointer] < prices[leftPointer]:
                leftPointer = rightPointer
            rightPointer += 1
        return maxProfit
