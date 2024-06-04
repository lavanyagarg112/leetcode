class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        prev = 0
        maxNum = 0
        flag = True

        for i in nums:
            if flag:
                maxNum = i
                prev = i
                flag = False
                continue

            prev = max(i + prev, i)

            maxNum = max(prev, maxNum)

        return maxNum