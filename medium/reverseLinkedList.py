# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        def helper(last, lst):

            if lst == None:
                return last
            else:
                return helper(ListNode(lst.val, last), lst.next)

        return helper(None, head)