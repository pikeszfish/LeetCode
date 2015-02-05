# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val < l2.val:
            ret = l1
            ret.next = self.mergeTwoLists(l1.next, l2)
        else:
            ret = l2
            ret.next = self.mergeTwoLists(l1, l2.next)
        return ret