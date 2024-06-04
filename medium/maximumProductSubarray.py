class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # so the issue right now is that how do we keep track of the negatives and the positives

        prevMax = 0
        prevMin = 0
        flag = True
        maxProd = 0
        minProd = 0

        for i in nums:
            if flag:
                flag = False
                prevMax = i
                prevMin = i
                maxProd = i
                minProd = i
                continue

            prevMinTemp = min(prevMin*i, i, prevMax*i)
            prevMax = max(prevMax*i, i, prevMin*i)
            prevMin = prevMinTemp
            maxProd = max(prevMax, maxProd)
            minProd = min(minProd, prevMin)


        return maxProd