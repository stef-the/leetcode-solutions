class Solution:
    def romanToInt(self, s: str) -> int:
        roman={
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        output=0
        for i in range(len(s)):
            if roman[s[i]] < roman[(s+"I")[i+1]]:
                output-=roman[s[i]]
            else:
                output+=roman[s[i]]
        return output
