# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if not head:
            return None
        f = head
        top = ListNode(f.val)
        c = top
        while f:
            f = f.next
            if f and f.val != c.val:
                c.next = ListNode(f.val)
                c = c.next
        return top
