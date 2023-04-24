import numpy as np
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max1 = 0
        max2 = 0
        while len(stones)>1:
            index = np.argmax(stones)
            max1 = stones[index]
            del stones[index]
            index = np.argmax(stones)
            max2 = stones[index]
            del stones[index]
            if max1 == max2:
                pass
            else:
                new = max1-max2
                stones.append(new)
        if len(stones) == 0:
            return 0
        return stones[0]
