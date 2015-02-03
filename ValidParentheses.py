class Node:
    def __init__(self, s, n):
        self.s = s
        self.next = n

class Solution:
    # @return a boolean
    def isValid(self, s):
        if not s:
            return False
        top = Node(s[0], None)
        for i in range(1, len(s)):
            if not top and (s[i] == '}' or s[i] == ']' or s[i] == ')'):
                return False
            if (s[i] == ')' and top.s == '(') or \
               (s[i] == ']' and top.s == '[') or \
               (s[i] == '}' and top.s == '{'):
                top = top.next
            else:
                a = Node(s[i], top)
                top = a
        return False if top else True