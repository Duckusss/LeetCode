class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        curr = m + n - 1
        m = m - 1
        n = n - 1
        while n >= 0:
            num1_curr = nums2[0]-1 if m < 0 else nums1[m]
            if num1_curr > nums2[n]:
                nums1[curr] = num1_curr
                m -= 1
            else:
                nums1[curr] = nums2[n]
                n -= 1
            curr -= 1
