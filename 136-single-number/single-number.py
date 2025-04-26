class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        uni=set()
        dup=set()
        for i in range(len(nums)):
            if nums[i] not in uni:
                uni.add(nums[i])
            else:
                dup.add(nums[i]) 
        return (uni-dup).pop()  
        