class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        s1 = {}
        
        for i in s:
            count = 0
            if i in s1:
                count = s1[i]
            s1[i] = count + 1

        for i in t:
            if i in s1 and s1[i] > 0:
                s1[i] -= 1
            else:
                return False

            if s1[i] == 0:
                s1.pop(i)

        return len(s1) == 0