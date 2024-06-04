class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        stack = []
        d = {'(': ')', '{' : '}', '[' : ']'}

        for i in s:
            if i in '({[':
                stack.append(d[i])

            else:
                if len(stack) == 0 or stack.pop() != i:
                    return False

        return len(stack) == 0