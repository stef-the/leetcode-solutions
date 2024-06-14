class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        o = ["(","[","{"]
        c = [")","]","}"]
        buffer = []
        for i in list(s):
            if i in o:
                buffer.append(o.index(i))
            else:
                if buffer == []:
                    return False
                elif i==c[buffer[-1]]:
                    buffer = buffer[:-1]
                else:
                    return False
        return True if buffer == [] else False
