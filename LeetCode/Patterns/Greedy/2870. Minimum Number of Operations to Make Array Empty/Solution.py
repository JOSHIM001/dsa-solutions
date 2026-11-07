from collections import Counter
import math
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        freq=Counter(nums)
        ans=0
        for f in freq.values():
            if f==1:
                return -1
            ans+=math.ceil(f/3)
        return ans