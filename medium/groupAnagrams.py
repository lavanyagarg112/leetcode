class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        # use sets

        d = {}
        duplicate = {}
        result = []
        ident = 0


        for i in strs:
            myset = frozenset(i)
            if len(i) != len(myset):
                count = {}
                for c in i:
                    if c in count:
                        count[c] += 1
                    else:
                        count[c] = 1

                myset = frozenset(count.items())


            if myset in d:
                d[myset].append(i)
            else:
                d[myset] = [i]



        for i in d:
            result.append(d[i])

        return result