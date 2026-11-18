class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = len(height) - 1
        left = height[i]
        right = height[j]
        max_volume = min(left, right)*(j-i)
        while i != j:
            if height[i] > height[j]:
                j -= 1
                if right < height[j]:
                    right = height[j]
                    max_volume = max(max_volume, min(left, right)*(j-i))
            else:
                i += 1
                if left < height[i]:
                    left = height[i]
                    max_volume = max(max_volume, min(left, right)*(j-i))
        return max_volume
