class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        p = m - 1
        q = n -1

        for i in range(m + n - 1, - 1, -1):
            if q < 0: 
                break

            
            if p >= 0 and nums1[p] > nums2[q]:
                nums1[i] = nums1[p]
                p -= 1

            else:
                nums1[i] = nums2[q]
                q -= 1