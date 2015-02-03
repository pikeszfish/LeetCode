# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None
        alen = 0
        t = headA
        while t:
            alen += 1
            t = t.next
        blen = 0
        t = headB
        while t:
            blen += 1
            t = t.next
        s = alen - blen if alen > blen else blen - alen
        at = headA
        bt = headB
        if alen > blen:
            while s > 0:
                at = at.next
                if at == None:
                    return None
                s -= 1
        else:
            while s > 0:
                bt = bt.next
                if bt == None:
                    return None
                s -= 1
        while at != None and bt != None:
            if at == bt:
                return at
            at = at.next
            bt = bt.next
        return None