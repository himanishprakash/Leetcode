class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        merged = sorted(nums1 + nums2)
        
        n = len(merged)
        median = n // 2
        if n % 2== 1:
            return merged[median]
        else:
            return (merged[median - 1] + merged[median]) / 2