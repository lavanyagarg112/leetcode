# First Attempt

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        d1 = {}
        d2 = {}

        for i in nums1:
            if i in d1:
                d1[i] += 1
            else:
                d1[i] = 1

        for i in nums2:
            if i in d2:
                d2[i] += 1
            else:
                d2[i] = 1

        s1 = set(frozenset(nums1))
        s2 = set(frozenset(nums2))

        s = s1.intersection(s2)

        result = []

        for i in s:
            freq = min(d1[i], d2[i])
            for j in range(freq):
                result.append(i)

        return result