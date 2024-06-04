# Definition for singly-linked list:
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        ref = set()
        
        def helper(lst):

            if lst == None or lst.next == None:
                return False

            elif lst in ref:
                return True

            else:
                ref.add(lst)
                return helper(lst.next)

        return helper(head)