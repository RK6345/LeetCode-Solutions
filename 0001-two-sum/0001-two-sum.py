class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for i,k in enumerate(nums):
            d[k]=i
        
        for i in range(len(nums)):
            x=target-nums[i]

            if x in d and d[x] != i:
                return [i,d[x]]

                