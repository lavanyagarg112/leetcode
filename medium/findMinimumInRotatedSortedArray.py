# Understanding the question

'''
Simply a rotated sorted array and we need to find the min
it is rotated between 1 and n times
n = length of array

Time complexity required: O(log n) -> BINARY SEARCH
'''

# Brainstorming the solution

'''
Like searching in a rotated sorted array
But instead of searching for a target, i just keep updating the min
we have TT...TF...F
need to find the first false
or the first true if we look at it the other way round
'''


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        ans = nums[0]

        begin = 0
        end = len(nums) - 1

        while begin <= end:
            mid = begin + (end - begin)//2
            startNum = nums[begin]
            endNum = nums[end]

            if nums[mid] < ans:
                ans = nums[mid]

            if nums[mid] >= startNum and nums[mid] >= endNum: # can simply do nums[mid] >= endNum cause if it is >= endNum, it has to be >= startNum
                begin = mid + 1

            else:
                end = mid - 1

        return ans
        
