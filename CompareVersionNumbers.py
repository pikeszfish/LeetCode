class Solution:
    # @param version1, a string
    # @param version2, a string
    # @return an integer
    def compareVersion(self, version1, version2):
        while version1 and version2:
            v1 = version1.split('.', 1)
            v2 = version2.split('.', 1)
            if int(v1[0]) > int(v2[0]):
                return 1
            elif int(v1[0]) < int(v2[0]):
                return -1
            version1 = v1[1]
            version2 = v2[1]
        if version1:
            for i in version1.split('.'):
                if int(i) > 0:
                    return 1
            return 0
        if version2:
            for i in version2.split('.'):
                if int(i) > 0:
                    return 1
            return 0
