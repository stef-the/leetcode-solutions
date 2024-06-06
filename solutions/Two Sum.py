class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a=len(nums)
        for i in range(a):
            for j in range(i+1,a):
                if nums[i]+nums[j]==target:
                    return [i,j]
