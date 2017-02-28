class Solution:
    # @param version1, a string
    # @param version2, a string
    # @return an integer
    def compareVersion(self, version1, version2):
        v1 = version1.split('.')
        v2 = version2.split('.')
        for i in range(0, min(len(v1), len(v2))):
            if int(v1[i]) > int(v2[i]):
                return 1
            if int(v1[i]) < int(v2[i]):
                return -1
        if len(v1) == len(v2):
            return 0
        elif len(v1) > len(v2):
            for i in range(len(v2), len(v1)):
                if int(v1[i]) != 0:
                    return 1
            return 0
        else:
            for i in range(len(v1), len(v2)):
                if int(v2[i]) != 0:
                    return -1
            return 0

