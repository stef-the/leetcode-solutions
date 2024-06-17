class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        startprefix = strs[0]
        for i in strs:
            while i[:len(startprefix)] != startprefix:
                startprefix=startprefix[:-1]
        return startprefix
