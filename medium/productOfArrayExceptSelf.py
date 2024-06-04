class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        if len(nums) == 0:
            return [0]

        prefix = []
        preprev = 1
        suffix = []
        presuf = 1

        for i in nums:
            prefix.append(0)
            suffix.append(0)

        for i in range(len(nums)):
            prefix[i] = preprev
            preprev *= nums[i]

        for i in range(len(nums)-1, -1, -1):
            suffix[i] = presuf
            presuf *= nums[i]

        for i in range(len(nums)):
            nums[i] = prefix[i] * suffix[i]

        return nums