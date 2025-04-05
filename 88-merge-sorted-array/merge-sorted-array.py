class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        for i in range(m+n):
            if i>=m:
                nums1.pop(m)
        for i in (nums2):
            nums1.append(i) 
        nums1.sort()        

        return nums1   
    