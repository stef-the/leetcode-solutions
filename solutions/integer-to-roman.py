class Solution:
    def intToRoman(self, num: int) -> str:
        roman_nums = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
        a,out=0,""
        while num>0:
            if roman_nums[a][0]<=num:
                num-=roman_nums[a][0]
                out+=roman_nums[a][1]
            else:
                a+=1
        return out
