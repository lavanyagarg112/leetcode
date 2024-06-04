class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """

        intervals.sort()
        
        output = []
        start = 0
        end = 0
        flag = False
        for index in range(len(intervals)):
            i = intervals[index]
            if not flag:
                start = i[0]
                end = i[1]
                flag = True

            else:
                if i[0] <= end:
                    end = max(end,i[1])
                else:
                    output.append([start, end])
                    start = i[0]
                    end = i[1]

            if index == len(intervals) - 1:
                output.append([start, end])


        return output