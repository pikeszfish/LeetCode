class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if not strs:
            return ''
        strs.sort(cmp=lambda a, b: len(a)-len(b))
        s = strs[0]
        for i in range(1, len(strs)):
            if strs[i].startswith(s):
                continue
            else:
                s = s[:-1]
                while s:
                    if strs[i].startswith(s):
                        break
                    else:
                        s = s[:-1]
                if not s:
                    return ''
        return s

a = Solution()
print a.longestCommonPrefix(["aa","a"])