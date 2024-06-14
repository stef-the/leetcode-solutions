class Solution(object):
    def minIncrementForUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = 0
        j = 0
        nums.sort()
        for i in nums:
            j = max(j, i)
            counter += j - i
            j += 1
        return counter
