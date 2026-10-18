class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        f1 = f2 = 0
        for i in range(len(cost)-1):
            f1, f2 = f2, min(f1 + cost[i], f2 + cost[i+1])
        return f2
