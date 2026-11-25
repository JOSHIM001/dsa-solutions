class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dit={}
        t=0
        for i,n in enumerate(nums):
            t=target-n
            if t in dit:
                return [dit[t],i]
            else:
                dit[n]=i


