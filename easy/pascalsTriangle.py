class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        if numRows < 1:
            return []

        output = []

        for row in range(numRows):
            temp = []
            for col in range(row + 1):
                if row == 0 or col == 0 or col == row:
                    temp.append(1)
                else:
                    num = output[row - 1][col - 1] + output[row - 1][col]
                    temp.append(num)

            output.append(temp)

        return output
