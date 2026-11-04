from collections import defaultdict

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        groups = defaultdict(list)
        
        for item in nums:
            groups[item].append(item)

        seperated_groups = list(groups.values())
        return [x for x in seperated_groups if len(x) == 1][0][0]
