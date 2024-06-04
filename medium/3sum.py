class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        # like 2 sum
        # but this is find 0 - this, then 2 sum algo

        if set(frozenset(nums)) == set(frozenset([0])):
            return [[0,0,0]]

        result = []
        result_set = set()
        length = range(len(nums))

        def checkSet(arrSet):
            return arrSet not in result_set

        def check(i,j,k):
            return i != j and j != k and i != k


        for j in length:
            target = 0 - nums[j]
            d = {}
            for i in length:
                n = nums[i]
                if n in d:
                    index = d[n]
                    arr = [0 - target, nums[index], nums[i]]
                    arrSet = frozenset(arr)
                    if check(i,j,index) and checkSet(arrSet):
                        result.append(arr)
                        result_set.add(arrSet)
                        

                else:
                    d[target - n] = i

        return result