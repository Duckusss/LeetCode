class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        stones.sort()
        while len(stones) > 1:
            samuel_stones = stones[-2]
            robert_rocks = stones[-1]
            stones = stones[:-2]
            if samuel_stones != robert_rocks:
                bisect.insort(stones, robert_rocks - samuel_stones)
        return stones[0] if stones else 0
